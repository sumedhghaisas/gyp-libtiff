{    
    'targets': [
    {
      'target_name': 'tiff_test',
      'dependencies': [
        '../bindings/libtiff.gyp:libtiff'
      ],
      'sources': [
        
      ],
      "include_dirs": [
        "../libtiff/libtiff/",
	"../config/<(OS)/<(target_arch)"
      ],
    }
  ]
}
