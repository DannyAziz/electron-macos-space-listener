#include <node_api.h>
#include "SpaceChangeListener.h"

napi_ref js_callback_ref;
napi_env global_env; // Store the napi_env globally

void space_change_callback() {
    // This function will be called from Swift when the space changes
    // Call the stored JavaScript callback
    napi_handle_scope scope;
    napi_open_handle_scope(global_env, &scope);

    napi_value global;
    napi_value js_callback;

    napi_get_global(global_env, &global);
    napi_get_reference_value(global_env, js_callback_ref, &js_callback);

    if (js_callback != NULL) {
        napi_value result;
        napi_call_function(global_env, global, js_callback, 0, NULL, &result);
    }

    napi_close_handle_scope(global_env, scope);
}

napi_value StartSpaceChangeListener(napi_env env, napi_callback_info info) {
    global_env = env; // Store the env for later use

    size_t argc = 1;
    napi_value args[1];
    napi_value js_callback;

    napi_get_cb_info(env, info, &argc, args, NULL, NULL);
    if (argc >= 1) {
        js_callback = args[0];
        napi_create_reference(env, js_callback, 1, &js_callback_ref);
    }

    startSpaceChangeListener(space_change_callback);
    return NULL;
}

napi_value Init(napi_env env, napi_value exports) {
    napi_status status;
    napi_value fn;

    status = napi_create_function(env, NULL, 0, StartSpaceChangeListener, NULL, &fn);
    if (status != napi_ok) return NULL;

    status = napi_set_named_property(env, exports, "startSpaceChangeListener", fn);
    if (status != napi_ok) return NULL;

    return exports;
}

NAPI_MODULE(NODE_GYP_MODULE_NAME, Init)