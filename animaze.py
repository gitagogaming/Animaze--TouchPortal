import json
import websocket
import logging

class AnimazeWrapper:
    """
    A Python wrapper for the Animaze API.

    Args:
        dev_name (str): The developer name or identifier. Defaults to "MyDevName".
        websocket_url (str, optional): The URL of the WebSocket server. Defaults to "ws://localhost:9000".

    Attributes:
        dev_name (str): The developer name or identifier.
        websocket_url (str): The URL of the WebSocket server.
        ws (websocket._core.WebSocket): The WebSocket connection object.
        logger (logging.Logger): The logger object for logging messages.
    """
    def __init__(self, dev_name="MyDevName", websocket_url="ws://localhost:9000"):
        self.dev_name = dev_name
        self.websocket_url = websocket_url
        self.ws = None
        self.logger = logging.getLogger(__name__)
        
    def onMessage(self, message):
        """
        Called when a WebSocket message is received.
        Override this method to handle incoming messages as per your requirements.
        """
        self.logger.info(f"Received message: {message}")

        # Add your message processing logic here
        # Example: If your WebSocket messages are JSON objects, you can parse them and act accordingly.

    def connect(self):
        try:
            self.ws = websocket.create_connection(self.websocket_url)
            self.onConnect()  # Call onConnect when connection is successful

            # Start a loop to listen for messages
            while True:
                message = self.ws.recv()
                if message is None:
                    break  # Connection closed, exit the loop
                self.onMessage(message)

            return self.ws
        except ConnectionRefusedError:
            self.logger.error("Connection was actively refused by the target machine.")
            self.logger.error("Is Animaze running?")
            return "Connection was actively refused by the target machine. Is Animaze running?"
        except Exception as e:
            self.logger.error(f"Failed to open WebSocket due to: {str(e)}")
            return

   #def connect(self):
   #    try:
   #        self.ws = websocket.create_connection(self.websocket_url)
   #        self.logger.info("WebSocket connection opened successfully.")
   #        return self.ws
   #    except ConnectionRefusedError:
   #        self.logger.error("Connection was actively refused by the target machine.")
   #        self.logger.error("Is Animaze running?")
   #        return "Connection was actively refused by the target machine. Is Animaze running?"
   #    except Exception as e:
   #        self.logger.error(f"Failed to open WebSocket due to: {str(e)}")
   #        return
 


    def disconnect(self):
        if self.ws is not None:
            self.ws.close()
            self.ws = None
            self.logger.info("WebSocket connection closed successfully.")
            return "WebSocket connection closed successfully."
        else:
            self.logger.error("No WebSocket connection to close.")
            return "No WebSocket connection to close."

    def send_command(self, command):
        try:
            if self.ws is None:
                self.logger.error("WebSocket connection is not open. Call 'open_websocket' first.")
                return

            self.ws.send(json.dumps(command))
            response = self.ws.recv()
            return json.loads(response)
        except Exception as e:
            self.logger.error('Failed to send command due to: ' + str(e))


    
    def get_item_icon(self, avatar_name:str):
        command = {
            "action": "GetItemIcon",
            "id": self.dev_name,
            "name": avatar_name
        }
        return self.send_command(command)


    def get_idle_anims(self):
        command = {
            "action": "GetIdleAnims",
            "id": self.dev_name
        }
        return self.send_command(command)


    def get_special_actions(self):
        command = {
            "action": "GetSpecialActions",
            "id": self.dev_name
        }
        return self.send_command(command)

    def get_poses(self):
        command = {
            "action": "GetPoses",
            "id": self.dev_name
        }
        return self.send_command(command)
    

    def get_emotes(self):
        command = {
            "action": "GetEmotes",
            "id": self.dev_name
        }
        return self.send_command(command)

    def get_cameraTransform(self):
        command = {
            "action": "GetCameraTransform",
            "id": self.dev_name
        }
        return self.send_command(command)

    def set_camera_transform(self,
                            pos_x:float, pos_y:float, pos_z:float,
                            rot_x:float, rot_y:float, rot_z:float, rot_w:float
                            ):
        command = {
            "action": "SetCameraTransform",
            "position":[pos_x, pos_y, pos_z],
            "rotation":[rot_x, rot_y, rot_z, rot_w]
        }
        return self.send_command(command)


    def get_camera_fov(self):
        command = {
            "action": "GetCameraFOV",
            "id": self.dev_name
        }
        return self.send_command(command)


    def set_camera_fov(self, fov:float):
        command = {
            "action": "SetCameraFOV",
            "id": self.dev_name,
            "fov": fov
        }
        return self.send_command(command)


    def broadcast(self, choice:bool):
        command = {
            "action": "Broadcast",
            "id": self.dev_name,
            "toggle": choice
        }
        return self.send_command(command)

    def trigger_special_action(self, index:int):
        command = {
            "action": "TriggerSpecialAction",
            "id": self.dev_name, 
            "index": index
           }
        return self.send_command(command)
    
    def trigger_idle_anim(self, index:int):
        command = {
            "action": "TriggerIdle",
            "id": self.dev_name, 
            "index": index
        }
        return self.send_command(command)
    

    def trigger_emote(self, anim_name:str):
        command = {
            "action": "TriggerEmote",
            "id": self.dev_name, 
            "itemName": anim_name
        }
        return self.send_command(command)


    def trigger_pose(self, pose_index:int):
        command = {
            "action": "TriggerPose",
            "id": self.dev_name, 
            "index": pose_index
        }
        return self.send_command(command)

    def get_scenes(self):
        command = { 
            "action": "GetScenes",
            "id": self.dev_name
        }
        return self.send_command(command)
    
    def get_quickscenes(self):
        command = { 
            "action": "GetQuickscenes",
            "id": self.dev_name
        }
        return self.send_command(command)

    def load_scene(self, scene_name:str):
        command = {
            "action": "LoadScene",
            "id": self.dev_name,
            "name": scene_name
        }
        return self.send_command(command)
    

    def load_quick_scene(self, scene_index:int):
        command = {
            "action": "LoadQuickscene",
            "id": self.dev_name,
            "index": scene_index
        }
        return self.send_command(command)
    

    def get_avatars(self):
        command = {
			"action": "GetAvatars",
			"id": self.dev_name
		}
        return self.send_command(command)
    
    def load_avatar(self, avatar_name:str):
        command = {
            "action": "LoadAvatar",
            "id": self.dev_name,
            "name": avatar_name
        }
        return self.send_command(command)
    

    def cross_eyes(self, choice:bool):
        command = {
            "action": "SetOverride",           
            "behavior": "Cross Eyes",            
            "value": choice
        }
        return self.send_command(command)

    def auto_blink(self, choice:bool, frequency:float):
        command = {
            "action": "SetOverride",           
            "behavior": "Auto Blink",            
            "value": choice,
            "frequency": frequency
        }
        return self.send_command(command)
    
    def look_at_camera(self, choice:bool):
        command = {
            "action": "SetOverride",           
            "behavior": "Look At Camera",            
            "value": choice
            ## "range": 0.5
        }
        return self.send_command(command)
    

    def mousekeyboard_behavior(self, choice:bool, keyboardScale:float, handToKeyboardDist:float, xOffset:float, yOffset:float, zOffset:float):
        """ 
        Sets the location of mouse & keyboard in relation to model
        """
        command = {
            "action": "SetOverride",                   
            "behavior": "Mouse Keyboard Behavior",     
            "value": choice,                           
            "keyboardScale": keyboardScale,            
            "handToKeyboardDist": handToKeyboardDist,  
            "xAxisOffset": xOffset,                    
            "yAxisOffset": yOffset,                    
            "zAxisOffset ": zOffset                    
        }
        return self.send_command(command)



    def follow_mouse(self, choice:bool):
        """ 
        Enable or disable the follow mouse behavior
        - choice: True or False
        """
        command ={
            "action": "SetOverride",            # required (string) 
            "behavior": "Follow Mouse Cursor",  # required (string)
            "value": choice                     # required (bool)
        }
        return self.send_command(command)
    
    def pupil_behavoior(self, value:bool, frequency:float=None):
        """ Adjust how often the pupils move 
            - value: True or False
            - frequency (optional): 0.0 - 1.0
            """
        command = {
            "action": "SetOverride",          
            "behavior": "Pupil Behavior",    
            "value": value,                
            "frequency": frequency        
        }
        return self.send_command(command)
    

    def breathing_behavior(self, value:bool, amplitude:float, frequency:float):
        """ Adjust how often the pupils move
            - value: True or False
            - amplitude(optional): 0.0 - 1.0
            - frequency(optional): 0.0 - 1.0
            """
        command = {
            "action": "SetOverride",          
            "behavior": "Breathing Behavior", 
            "value": value,                  
            "amplitude": amplitude,           
            "frequency": frequency            
        }
        return self.send_command(command)
    


#wrapper = AnimazeWrapper("MyDevName")
#wrapper.connect()
#
##response = wrapper.cross_eyes(False)
#response = wrapper.pupil_behavoior(True, 0.5)
#print(response)
## Use send_command here to send commands using the open WebSocket connection
#import time
#time.sleep(5)
#wrapper.disconnect()
