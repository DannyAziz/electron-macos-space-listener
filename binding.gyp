{
  "targets": [
    {
      "target_name": "space_change_listener",
      "sources": [ "SpaceChangeListener.c" ],
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "libraries": [ "${PROJECT_DIR}/src/native/SpaceChangeListener.dylib" ],

      "xcode_settings": {
        "MACOSX_DEPLOYMENT_TARGET": "10.10",
        "GCC_ENABLE_CPP_RTTI": "YES",
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "CLANG_CXX_LIBRARY": "libc++",
        "OTHER_LDFLAGS": [
          "-Wl,-rpath,@loader_path/../Frameworks/",
          "-Wl,-rpath,@executable_path/../Frameworks/",
          "-Wl,-rpath,${PROJECT_DIR}/src/native/"
        ],
        "OTHER_CFLAGS": [
          "-I${PROJECT_DIR}/src/native"
        ],
        "LD_RUNPATH_SEARCH_PATHS": [
          "@executable_path/../Frameworks",
          "@loader_path/../Frameworks"
        ]
      },
    }
  ]
}