{
  "targets": [
    {
      "target_name": "addon",
      "sources": [ "addon.cc" ],
      "include_dirs" : [
        "<!(node -e \"require('nan')\")",
      ],
      "msvs_settings": {
        "VCCLCompilerTool": {
          "RuntimeTypeInfo": "false"
          , "ExceptionHandling": 1
          , "DisableSpecificWarnings": [ "4355", "4530" ,"4267", "4244", "4506" ]
        }
      },
      "configurations": {
        "Release": {
          "msvs_settings": {
            "VCCLCompilerTool": {
              "ExceptionHandling": 1
            }
          }
        }
      }
    }
  ]
}
