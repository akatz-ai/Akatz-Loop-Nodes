from .utility_nodes import UTILITY_NODE_CLASS_MAPPINGS, UTILITY_NODE_DISPLAY_NAME_MAPPINGS
from .latent_nodes import LATENT_NODE_CLASS_MAPPINGS, LATENT_NODE_DISPLAY_NAME_MAPPINGS
from .image_nodes import IMAGE_NODE_CLASS_MAPPINGS, IMAGE_NODE_DISPLAY_NAME_MAPPINGS, SmartLoopPreviewImage
from .flow_control import FLOW_CONTROL_NODE_CLASS_MAPPINGS, FLOW_CONTROL_NODE_DISPLAY_NAME_MAPPINGS
from .lazy_nodes import GENERAL_NODE_CLASS_MAPPINGS, GENERAL_NODE_DISPLAY_NAME_MAPPINGS

# Register execution_start handler to reset SmartLoopPreviewImage accumulators
from server import PromptServer
from aiohttp import web

@PromptServer.instance.routes.post("/akatz-loops/reset_preview_accumulators")
async def reset_preview_accumulators(request):
    SmartLoopPreviewImage.reset_accumulator()
    return web.json_response({"status": "ok"})

# Hook into execution_start event
original_send_sync = PromptServer.instance.send_sync

def patched_send_sync(event, data, sid=None):
    if event == "execution_start":
        SmartLoopPreviewImage.reset_accumulator()
    return original_send_sync(event, data, sid)

PromptServer.instance.send_sync = patched_send_sync

NODE_CLASS_MAPPINGS = {}
NODE_CLASS_MAPPINGS.update(UTILITY_NODE_CLASS_MAPPINGS)
NODE_CLASS_MAPPINGS.update(LATENT_NODE_CLASS_MAPPINGS)
NODE_CLASS_MAPPINGS.update(IMAGE_NODE_CLASS_MAPPINGS)
NODE_CLASS_MAPPINGS.update(FLOW_CONTROL_NODE_CLASS_MAPPINGS)
NODE_CLASS_MAPPINGS.update(GENERAL_NODE_CLASS_MAPPINGS)


NODE_DISPLAY_NAME_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS.update(UTILITY_NODE_DISPLAY_NAME_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(LATENT_NODE_DISPLAY_NAME_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(IMAGE_NODE_DISPLAY_NAME_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(FLOW_CONTROL_NODE_DISPLAY_NAME_MAPPINGS)
NODE_DISPLAY_NAME_MAPPINGS.update(GENERAL_NODE_DISPLAY_NAME_MAPPINGS)
