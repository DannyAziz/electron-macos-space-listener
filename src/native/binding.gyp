{
  "targets": [
    {
      "target_name": "spaceChangeListener",
      "sources": [ "SpaceChangeListener.c" ],
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "product_dir": "${PROJECT_DIR}/dist",
      "libraries": [ "${PROJECT_DIR}/dist/SpaceChangeListener.dylib" ],

      "xcode_settings": {
        "MACOSX_DEPLOYMENT_TARGET": "10.10",
        "GCC_ENABLE_CPP_RTTI": "YES",
        "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
        "CLANG_CXX_LIBRARY": "libc++",
        "OTHER_LDFLAGS": [
          "-Wl,-rpath,@loader_path/../Frameworks/",
          "-Wl,-rpath,@executable_path/../Frameworks/",
          "-Wl,-rpath,${PROJECT_DIR}/dist/"
        ],
        "OTHER_CFLAGS": [
          "-I${PROJECT_DIR}/dist"
        ],
        "LD_RUNPATH_SEARCH_PATHS": [
          "@executable_path/../Frameworks",
          "@loader_path/../Frameworks"
        ]
      },
    }
  ]
}