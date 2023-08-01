PLUGIN_ID = "gitago.Animaze"
PLUGIN_NAME = "Animaze_Plugin"
PLUGIN_FOLDER = "Animaze"
PLUGIN_ICON = "animaze_logo.png"



TP_PLUGIN_INFO = {
    "sdk": 6,
    "version": 100,
    "name": "Animaze",
    "id": PLUGIN_ID,
    "plugin_start_cmd_windows": f"%TP_PLUGIN_FOLDER%{PLUGIN_FOLDER}\\{PLUGIN_NAME}.exe",
    "configuration": {
        "colorDark": "#222423",
        "colorLight": "#43a047"
    },
    "plugin_start_cmd": f"%TP_PLUGIN_FOLDER%{PLUGIN_FOLDER}\\{PLUGIN_NAME}.exe"
}



TP_PLUGIN_SETTINGS = {
    "1": {
        "name": "Debug",
        "default": "False",
        "type": "text"
    }
}



TP_PLUGIN_CATEGORIES = {
    "main": {
        "id": PLUGIN_ID + ".main",
        "name": "Animaze",
        "imagepath": f"%TP_PLUGIN_FOLDER%Animaze\\{PLUGIN_ICON}"
    }
}

TP_PLUGIN_CONNECTORS = {}



TP_PLUGIN_ACTIONS = {
    "1": {
        "id": PLUGIN_ID + ".act.selectAvatar",
        "name": "Select an Avatar",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "format": "Change Avatar to $[1]",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.selectAvatar.choice",
                "type": "choice",
                "label": "The Avatar to Select",
                "default": "",
                "valueChoices": []
            }
        },
        "category": "main"
    },
  
    "2": {
        "id": PLUGIN_ID + ".act.selectScene",
        "name": "Select an Scene",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "format": "Change Scene to $[1]",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.selectScene.choice",
                "type": "choice",
                "label": "The Scene to Select",
                "default": "",
                "valueChoices": []
            }
        },
        "category": "main"
    },
    "3": {
        "id": PLUGIN_ID + ".act.selectQuickScene",
        "name": "Select an QuickScene",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "format": "Change QuickScene to $[1]",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.selectQuickScene.choice",
                "type": "choice",
                "label": "The QuickScene to Select",
                "default": "",
                "valueChoices": []
            }
        },
        "category": "main"
    },

    "4": {
        "id": PLUGIN_ID + ".act.selectPose",
        "name": "Select a Pose",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "format": "Change Pose to $[1]",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.selectPose.choice",
                "type": "choice",
                "label": "The Pose to Select",
                "default": "",
                "valueChoices": []
            }
        },
        "category": "main"
    },

    "5": {
        "id": PLUGIN_ID + ".act.selectEmote",
        "name": "Trigger an Emote",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "format": "Trigger the Emote:$[1]",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.selectEmote.choice",
                "type": "choice",
                "label": "The Emote to Select",
                "default": "",
                "valueChoices": []
            }
        },
        "category": "main"
    },

    "6": {
        "id": PLUGIN_ID + ".act.selectIdleAnim",
        "name": "Trigger an Idle Animation",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "format": "Change Idle Animation to $[1]",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.selectIdleAnim.choice",
                "type": "choice",
                "label": "The Idle to Select",
                "default": "",
                "valueChoices": []
            }
        },
        "category": "main"
    },

    "7": {
        "id": PLUGIN_ID + ".act.setCamera_FOV",
        "name": "Select Camera FOV",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "format": "Change Camera FOV to $[1]",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.setCamera_FOV.choice",
                "type": "text",
                "label": "The FOV to Select",
                "default": "20",
            }
        },
        "category": "main"
    },

    "8": {
        "id": PLUGIN_ID + ".act.startBroadcast",
        "name": "Start Broadcast",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "format": "$[1] the Broadcast",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.startBroadcast.choice",
                "type": "choice",
                "label": "Start or Stop",
                "default": "Start",
                "valueChoices": ["Start", "Stop"]
            }
        },
        "category": "main"
    },

    "9": {
        "id": PLUGIN_ID + ".act.specialAction",
        "name": "Trigger Special Action",
        "prefix": "Prefix",
        "type": "communicate",
        "tryInline": True,
        "format": "Trigger Special Action $[1]",
        "data": {
            "1": {
                "id": PLUGIN_ID + ".act.specialAction.choice",
                "type": "choice",
                "label": "The Special Action to Trigger",
                "default": "",
                "valueChoices": []
            }
        }
    },
    "10": {
        "id": PLUGIN_ID + ".act.cameraFOV.adjust",
        "name": "Adjust Camera FOV",
        "prefix": TP_PLUGIN_CATEGORIES['main']['name'],
        "type": "communicate",
        "tryInline": True,
        "hasHoldFunctionality": True,
        "description": "Adjust the Camera FOV by a set amount - Available in OnHold as well",
        "format": "$[1] the Camera FOV by $[2]  ",
        "data": 
        {
        "1": {
            "id": PLUGIN_ID + ".act.cameraFOV.adjust.choice",
            "type": "choice",
            "label": "Increase or Decrease",
            "default": "Increase",
            "valueChoices": ["Increase", "Decrease"]
        },
        "ZoomControlIncrement":{
            "id": PLUGIN_ID + ".cameraFOV.increment",
            "type": "text",
            "label": "text",
            "default": "5"
          }
        }
    },
        
    "11": { 
        "id": PLUGIN_ID + ".act.setCameraTransform",
        "name": "Set Camera Transform",
        "prefix": TP_PLUGIN_CATEGORIES['main']['name'],
        "type": "communicate",
        "tryInline": True,
        "hasHoldFunctionality": True,
        "description": "Set the Camera Transform",
        "format": "Set Camera Transform to Position X:$[1] Y:$[2] Z:$[3] Rotation X:$[4] Y:$[5] Z:$[6] W:$[7]",
        "data":
        {
            "1": {
                "id": PLUGIN_ID + ".act.setCameraTransform.pos_x",
                "type": "text",
                "label": "Position X",
                "default": "0"
            },
            "2": {
                "id": PLUGIN_ID + ".act.setCameraTransform.pos_y",
                "type": "text",
                "label": "Position Y",
                "default": "0"
            },
            "3": {
                "id": PLUGIN_ID + ".act.setCameraTransform.pos_z",
                "type": "text",
                "label": "Position Z",
                "default": "0"
            },
            "4": {
                "id": PLUGIN_ID + ".act.setCameraTransform.rot_x",
                "type": "text",
                "label": "Rotation X",
                "default": "0"
            },
            "5": {
                "id": PLUGIN_ID + ".act.setCameraTransform.rot_y",

                "type": "text",
                "label": "Rotation Y",
                "default": "0"
            },
            "6": {
                "id": PLUGIN_ID + ".act.setCameraTransform.rot_z",
                "type": "text",
                "label": "Rotation Z",
                "default": "0"
            },
            "7": {
                "id": PLUGIN_ID + ".act.setCameraTransform.rot_w",
                "type": "text",
                "label": "Rotation W",
                "default": "1"
            }
        }
    },
            # send chatpal message to animaze
    "12": {
        "id": PLUGIN_ID + ".act.sendChatpalMessage",
        "name": "Send Chatpal Message",
        "prefix": TP_PLUGIN_CATEGORIES['main']['name'],
        "type": "communicate",
        "tryInline": True,
        "description": "Send Chatpal Message to Animaze",
        "format": "Send Chatpal Message $[1] - Use $[2]",
        "data":
        {   
            "1": {
                "id": PLUGIN_ID + ".act.sendChatpalMessage.message",
                "type": "text",
                "label": "The Chatpal Message to Send",
                "default": ""
            },
            "2": {
                "id": PLUGIN_ID + ".act.sendChatpalMessage.choice",
                "type": "choice",
                "label": "The Chatpal Message to Send",
                "default": "Local",
                "valueChoices": ["Local", "AI"]     
        }
        }
    }

    
   # "12": {
   #     "id": PLUGIN_ID + ".act.setOverride",
   #     "name": "Set Override",
   #     "prefix": TP_PLUGIN_CATEGORIES['main']['name'],
   #     "type": "communicate",
   #     "tryInline": True,
   #     "hasHoldFunctionality": True,
   #     "description": "Optional: Frequency for Cross Eyes",
   #     "format": "Set Override for $[1]  OPTIONAL:$[2]",
   #     "data":
   #     {
   #         "1": {
   #             "id": PLUGIN_ID + ".act.setOverride.choice",
   #             "type": "choice",
   #             "label": "The Override to Set",
   #             "default": "",
   #             "valueChoices":["Follow Mouse Cursor", "Auto Blink", "Look at Camera", "Look at Camera Head", "Cross Eyes"]#["Follow Mouse Cursor", "Mouse Keyboard Behavior", "Tracked Blinking", "Auto Blink",
   #                            #"Look At Camera", "Look At Camera Head", "Cross Eyes", "Pupil Behavior", "Forced Symmetry Eyebrows",
   #                            # "Forced Symmetry Eyelids", "Forced Symmetry Mouth", "Enhanced Body Movement 2D", "Enhanced Body Movement 3D",
   #                            # "Extreme Head Angles Attenuation", "Sound to Mouth Open", "Alternate lipsync Retargeting", "Idle Intensity",
   #                            # "Inferred Body Yaw Movement", "Breathing Behavior"]
   #         },
   #         "2": {
   #             "id": PLUGIN_ID + ".act.setOverride.frequency",
   #             "type": "text",
   #             "label": "Frequency",
   #             "default": "0"
   #         }
   #     }
   # }

            


}



TP_PLUGIN_STATES = {
    "0": {
        "id": PLUGIN_ID + ".state.currentAvatar",
        "type": "text",
        "desc": "Current Avatar",
        "default": "",
        "category": "main"
    },
    "1": {
        "id": PLUGIN_ID + ".state.currentAvatar.Image",
        "type": "text",
        "desc": "Current Avatar Image",
        "default": "",
        "category": "main"
    },
    "2": {
        "id": PLUGIN_ID + ".state.currentFOV",
        "type": "text",
        "desc": "Current Camera FOV",
        "default": "",
        "category": "main"
    },
    "3": {
        "id": PLUGIN_ID + ".state.currentScene",
        "type": "text",
        "desc": "Current Scene",
        "default": "",
        "category": "main"
    },
    "4": {
        "id": PLUGIN_ID + ".state.broadcastStatus",
        "type": "text",
        "desc": "Broadcast Status",
        "default": "",
        "category": "main"
    }

}



TP_PLUGIN_EVENTS = {}


