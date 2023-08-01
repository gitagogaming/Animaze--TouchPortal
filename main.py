# DONE ## Idle Anims need setup the same way that Special Actions is.. so the chocielist is numbered instead of named and it updates a list of states.. 
# DONE ## believe this is needed for quick scenes & poses as they are also indexed instead..
## setup SAVE quickscenes and then remember to make a video mention of how to use it with the same button.. so we make a 'set' button.. we press it then press the quickscene we are gonna override.. 
 

## set up sliders for camera transform.. with a single choice per axis.. and a slider for the rotation of the model itself maybe.. so it can spin?

import TouchPortalAPI
from TouchPortalAPI import TYPES
from TouchPortalAPI.logger import Logger
from TPPEntry import TP_PLUGIN_ACTIONS, TP_PLUGIN_STATES, TP_PLUGIN_EVENTS, PLUGIN_ID
import os
import webbrowser
import time
import ast

### Local Imports
from update_check import plugin_update_check, GITHUB_PLUGIN_NAME, GITHUB_USER_NAME, PLUGIN_NAME
from AnimazePy import AnimazeWrapper




TP_PATH = os.path.expandvars(rf'%APPDATA%\TouchPortal\plugins\{PLUGIN_NAME}')


class ClientInterface(TouchPortalAPI.Client):
    def __init__(self):
        super().__init__(self)
        
        
        self.pluginId = PLUGIN_ID
        # TP connection settings - These can be left at default
        self.TPHOST = "127.0.0.1"
        self.TPPORT = 12136
        self.RCV_BUFFER_SZ = 4096 
        self.SND_BUFFER_SZ = 1048576

        # Log settings
        self.logLevel = "INFO"
        self.setLogFile(PLUGIN_ID + "_LOG")
    
        # Register events
        self.add_listener(TYPES.onConnect, self.onConnect)
        self.add_listener(TYPES.onAction, self.onAction)
        self.add_listener(TYPES.onShutdown, self.onShutdown)
        self.add_listener(TYPES.onListChange, self.onListChange)
        self.add_listener(TYPES.onNotificationOptionClicked, self.onNoticationClicked)
        self.add_listener(TYPES.onSettingUpdate, self.onSettings)
        self.add_listener(TYPES.onHold_down, self.onHold_down)


    def settingsToDict(self, settings):
        """ 
        Convert a list of settings to a dictionary
        """
        return { list(settings[i])[0] : list(settings[i].values())[0] for i in range(len(settings)) }

    def update_idleAnims(self):
        idleAnims_response = animaze.get_idle_anims()
        self.idleAnims = {idleAnim['animName']: idleAnim['index'] for idleAnim in idleAnims_response['idleList']}
        self.idleAnims_list = [f"Idle Anim:{index}" for index, _ in enumerate(self.idleAnims)]
        plugin.choiceUpdate(PLUGIN_ID + ".act.selectIdleAnim.choice", values=list(self.idleAnims_list))
        for key, val in self.idleAnims.items():
            plugin.createState(stateId=PLUGIN_ID + f".state.idleAnim.{val}", description=f"Special Action:{val}", value=str(key), parentGroup="Idle Anims")

    def update_specialActions(self):
        special_actions_response = animaze.get_special_actions()
        self.special_actions = {special_action['animName']: special_action['index'] for special_action in special_actions_response['specialActions']}
        self.special_actions_list = [f"Special Action:{index}" for index, _ in enumerate(self.special_actions)]
        plugin.choiceUpdate(PLUGIN_ID + ".act.specialAction.choice", values=self.special_actions_list )
        for key, val in self.special_actions.items():
            plugin.createState(stateId=PLUGIN_ID + f".state.specialAction.{val}", description=f"Special Action:{val}", value=str(key), parentGroup="Special Actions")

    def update_Poses(self):
        pose_response = animaze.get_poses()
        self.pose_names = {pose['index']: pose['animName'] for pose in pose_response['poseList']}
        self.pose_names_list = [f"Pose:{index}" for index, _ in enumerate(self.pose_names)]
        plugin.choiceUpdate(PLUGIN_ID + ".act.selectPose.choice", values=self.pose_names_list )
        for key, val in self.pose_names.items():
            plugin.createState(stateId=PLUGIN_ID + f".state.pose.{key}", description=f"Pose:{key}", value=str(val), parentGroup="Poses")

    def update_quickScenes(self):
        quickScene_response = animaze.get_quickscenes()
        self.quickscenes = {quickscene['name']: quickscene['index'] for quickscene in quickScene_response['quickslots']}
        self.quickscenes_list = [f"Quick Scene:{index}" for index, _ in enumerate(self.quickscenes)]
        plugin.choiceUpdate(PLUGIN_ID + ".act.selectQuickScene.choice", values=list(self.quickscenes_list))
        for key, val in self.quickscenes.items():
            plugin.createState(stateId=PLUGIN_ID + f".state.quickScene.{val}", description=f"Quick Scene:{val}", value=str(key), parentGroup="Quick Scenes")

        


    """
    Events
    """
    def onConnect(self, data):
        self.log.info(f"Connected to TP v{data.get('tpVersionString', '?')}, plugin v{data.get('pluginVersion', '?')}.")
     #   self.log.info(self.settingsToDict(data["settings"]))
        self.log.debug(f"Connection: {data}")
        self.plugin_settings = self.settingsToDict(data["settings"])

        if animaze.ws == None:
            animaze.connect()


        try:
            ## Get Avatars for Choice List
            avatars_response = animaze.get_avatars()
            plugin.choiceUpdate(PLUGIN_ID + ".act.selectAvatar.choice", values=avatars_response['avatars'])

            ## Get Scenes for Choice List
            scenes_response = animaze.get_scenes()
            plugin.choiceUpdate(PLUGIN_ID + ".act.selectScene.choice", values=scenes_response['scenes'])

            ## Get Quick Scenes for Choice List
            self.update_quickScenes()

            ## Get Camera FOV
            cameraFOV_response = animaze.get_camera_fov()
            plugin.stateUpdate(PLUGIN_ID + ".state.camera_FOV", stateValue=cameraFOV_response['fov'])

            ## Get Idle Anims
            self.update_idleAnims()

            ## Get  Poses
            self.update_Poses()

            # Get Emotes
            emotes_response = animaze.get_emotes()
            self.emotes = {emote['friendlyName']: emote['itemName'] for emote in emotes_response['emotes']}
            plugin.choiceUpdate(PLUGIN_ID + ".act.selectEmote.choice", values=list(self.emotes.keys()))

            # Get Special Actions  
            self.update_specialActions()
        except TypeError as e:
            print("ERROR: ", e)
            
        ## Checking for Updates
        try:
            github_check, message = plugin_update_check(str(data['pluginVersion']))
            if github_check == True:
                plugin.showNotification(
                    notificationId= f"{PLUGIN_ID}.TP.Plugins.Update_Check",
                    title=f"{PLUGIN_NAME} {github_check} is available",
                    msg=f"A new version of {PLUGIN_NAME} is available and ready to Download.\nThis may include Bug Fixes and or New Features\n\nPatch Notes\n{message} ",
                    options= [{
                    "id":f"{PLUGIN_ID}.tp.update.download",
                    "title":"Click to Update!"
                }])
        except:
            print("Error Checking for Updates")



    def onSettings(self, data):
        self.plugin_settings = self.settingsToDict(data['values'])
        self.log.debug(f"Connection: {data}")

    def onAction(self, data):
        self.log.debug(f"Connection: {data}")


        if not (action_data := data.get('data')) or not (aid := data.get('actionId')):
            return
        
        if aid == PLUGIN_ID + ".act.selectAvatar":
            response = animaze.load_avatar(data['data'][0]['value'])
            if response:
                self.update_avatarSpecials(data['data'][0]['value'])
            self.log.debug(f"Avatar: {response}")

        if aid == PLUGIN_ID + ".act.selectScene":
            response = animaze.load_scene(data['data'][0]['value'])
            self.log.debug(f"Scene: {response}")

        if aid == PLUGIN_ID + ".act.selectQuickScene":
            stripped = int(data['data'][0]['value'].split(":")[-1].strip())
            response = animaze.load_quick_scene(stripped)
            self.log.debug(f"Quick Scene: {response}")

        if aid == PLUGIN_ID + ".act.selectPose":
            response = animaze.trigger_pose(int(data['data'][0]['value'].split(":")[-1].strip()))
            self.log.debug(f"Pose: {response}")

        if aid == PLUGIN_ID + ".act.selectEmote":
            response = animaze.trigger_emote(self.emotes[data['data'][0]['value']])
            self.log.debug(f"Emote: {response}")

        if aid == PLUGIN_ID + ".act.setCamera_FOV":
            response = animaze.set_camera_fov(float(data['data'][0]['value']))
            self.log.debug(f"Camera FOV Set: {response}")
            
        if aid == PLUGIN_ID + ".act.startBroadcast":
            match data['data'][0]['value']:
                case "Start":
                    choice = "true"
                case "Stop":
                    choice = "false"
            response = animaze.broadcast(bool(choice))
            self.log.debug(f"Broadcast: {response}")

        if aid == PLUGIN_ID + ".act.specialAction":
            stripped = int(data['data'][0]['value'].split(":")[-1].strip())
            response = animaze.trigger_special_action(stripped)
            self.log.debug(f"Special Action: {response}")

        if aid == PLUGIN_ID + ".act.selectIdleAnim":
            stripped = int(data['data'][0]['value'].split(":")[-1].strip())
            response = animaze.trigger_idle_anim(int(stripped))
            self.log.debug(f"Idle Anim: {response}")

        if aid == PLUGIN_ID + ".act.setOverride":
            response = None
            thebool = ast.literal_eval(data['data'][1]['value'].lower())

            match data['data'][0]['value']:
                case "Follow Mouse Cursor":
                    response = animaze.follow_mouse(thebool)
                case "Auto Blink":
                    response = animaze.auto_blink(thebool)
                case "Look at Camera":
                    response = animaze.look_at_camera(thebool)
                case "Look at Camera Head":
                    response = animaze.look_at_camera_head(thebool)
                case "Cross Eyes":
                    response = animaze.cross_eyes(thebool)

                

            if response:
                self.log.debug(f"Override: {response}")

        if aid == PLUGIN_ID + ".act.sendChatpalMessage":
            message = data['data'][0]['value']
            if data['data'][1]['value'] != "AI":
                message = f"-echo {data['data'][0]['value']}"

            response = animaze.send_chatpal_message(message)
            self.log.debug(f"Chatpal Message: {response}")


    def onNoticationClicked(data):
        if data['optionId'] == f'{PLUGIN_ID}.tp.update.download':
            github_check = TouchPortalAPI.Tools.updateCheck(GITHUB_USER_NAME, GITHUB_PLUGIN_NAME)
            url = f"https://github.com/{GITHUB_USER_NAME}/{GITHUB_PLUGIN_NAME}/releases/tag/{github_check}"
            webbrowser.open(url, new=0, autoraise=True)




    ## When a Choice List is Changed in a Button Action
    def onListChange(self, data):
        self.log.info(f"Connection: {data}")

    def onShutdown(self, data):
        self.log.info('Received shutdown event from TP Client.')
        self.disconnect()
        

    def onHold_down(self, data):
        try:
            if data['actionId'] == PLUGIN_ID + ".act.cameraFOV.adjust":
                # Get Current Camera FOV
                current_fov = animaze.get_camera_fov()
            elif data['actionId'] == PLUGIN_ID + ".act.setCameraTransform":
                # Get Current Camera Transform
                current_camera_transform = animaze.get_cameraTransform()

            while True:
                time.sleep(0.01)
                if plugin.isActionBeingHeld(PLUGIN_ID + ".act.cameraFOV.adjust"):
                    match data['data'][0]['value']:
                        case "Increase":
                            current_fov['fov'] += int(data['data'][1]['value'])
                        case "Decrease":
                            current_fov['fov'] -= int(data['data'][1]['value'])
                        case _:
                            break
                    animaze.set_camera_fov(float(current_fov['fov']))

                elif plugin.isActionBeingHeld(PLUGIN_ID + ".act.setCameraTransform"):
                    for index, x in enumerate(data['data']):
                        if x['value'] =="0" or x['value'] == "":
                            pass
                        else:
                            match index:
                                case 0:
                                    current_camera_transform['position'][0] += float(x['value'])
                                case 1:
                                    current_camera_transform['position'][1] += float(x['value'])
                                case 2:
                                    current_camera_transform['position'][2] += float(x['value'])
                                case 3:
                                    current_camera_transform['rotation'][0] += float(x['value'])
                                case 4:
                                    current_camera_transform['rotation'][1] += float(x['value'])
                                case 5:
                                    current_camera_transform['rotation'][2] += float(x['value'])
                                case 6:
                                    current_camera_transform['rotation'][3] += float(x['value'])
                                case _:
                                    break
                                
                    response = animaze.set_camera_transform(current_camera_transform['position'][0], 
                                                 current_camera_transform['position'][1],
                                                 current_camera_transform['position'][2],
                                                 current_camera_transform['rotation'][0],
                                                 current_camera_transform['rotation'][1],
                                                 current_camera_transform['rotation'][2],
                                                 current_camera_transform['rotation'][3])
                    if response:
                        response = animaze.get_camera_transform()
                        print(response)
                else:
                    break
        except Exception as e:
            self.log.debug(f"Error in TP Client event handler: {repr(e)}")
                #elif plugin.isActionBeingHeld(TP_PLUGIN_ACTIONS['Zoom Control OnHold']['id']):
                #    match data['data'][0]['value']:
                #        case "Lens X":
                #            magControl.magnifer_dimensions(x=True, y=None, onhold=int(data['data'][1]['value']))
                #        case "Lens Y":
                #            magControl.magnifer_dimensions(x=False, y=True, onhold=int(data['data'][1]['value']))
                #        case "Zoom":
                #            magControl.mag_level(int(data['data'][1]['value']), onhold=True)
                #        case _:
                #            break

  #  def onError(self, data):
  #      self.error(f'Error in TP Client event handler: {repr(data)}')

    def clear_states(self):
        """
        Clear all states related to the current avatar
        """
        current_states = plugin.getStatelist()
        for key, val in current_states.items():
            if "specialAction." in key or "idleAnim." in key or "pose." in key:
                plugin.stateUpdate(key, stateValue="")


    def update_avatarSpecials(self, avatar_name):
        ## Get Avatar Image
        avatar_response = animaze.get_item_icon(avatar_name)
        plugin.stateUpdate(PLUGIN_ID + ".state.currentAvatar", stateValue=avatar_name)
        plugin.stateUpdate(PLUGIN_ID + ".state.currentAvatar.Image", stateValue=avatar_response['image']) 

        ## Clear all related states
        self.clear_states()
        ## Get Idle Anims
        self.update_idleAnims()
        # Get Special Actions
        self.update_specialActions()
        ## Get Poses
        self.update_Poses()





#G_LOG = Logger(name = PLUGIN_ID)


plugin = ClientInterface()
animaze = AnimazeWrapper()



if __name__ == "__main__":
    ret = 0
    try:
        plugin.log.info("Connecting to TP Client...")
        plugin.connect()
    except KeyboardInterrupt:
        plugin.log.warning("Caught keyboard interrupt, exiting.")
    except Exception:
        from traceback import format_exc
        plugin.log.error(f"Exception in TP Client:\n{format_exc()}")
        ret = -1
    finally:
        plugin.disconnect()
        del plugin
        exit(ret)








    #async def send_command(self, command ):
    #    try:
    #        async with websockets.connect("ws://localhost:9000") as websocket:
    #                await websocket.send(json.dumps(command))
    #                response = None
    #                try:
    #                    response = await asyncio.wait_for( websocket.recv(), timeout=30 )
    #                except asyncio.TimeoutError:
    #                    print( f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')} receive\t >> TIMEOUT\n" )	
    #                return json.loads(response)
    #    except Exception as e:
    #        print( 'Failed due to: ' + str(e))
    #        if "remote computer refused" in str(e):
    #            print("Is Animaze running?")
    #        #log( logFile, 'Failed due to: ' + str(e) )
    #    pass



    #
#  special_actions_response = animaze.get_special_actions()
#  self.special_actions = {special_action['animName']: special_action['index'] for special_action in special_actions_response['specialActions']}
#  self.special_actions_list = [f"Special Action:{index}" for index, _ in enumerate(self.special_actions)]
#
#  if len(self.special_actions_list) > 0:
#      for key, val in self.special_actions.items():
#          #print(key, val)
#          plugin.createState(stateId=PLUGIN_ID + f".state.specialAction.{val}", description=f"Special Action:{val}", value=str(key))
#  else:
#      current_states = plugin.getStatelist()
#      for key, val in current_states.items():
#          if "specialAction." in key:
#              plugin.stateUpdate(key, stateValue="")
#
#  plugin.choiceUpdate(PLUGIN_ID + ".act.specialAction.choice", values=self.special_actions_list )