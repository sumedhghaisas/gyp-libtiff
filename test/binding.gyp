{    
    'targets': [
    {
      'target_name': 'tiff_test',
      'dependencies': [
        '../bindings/libtiff.gyp:libtiff'
      ],
	  'defines': [ 'NEED_LIBPORT' ],
      'sources': [
        "bmp2tiff.c",
		"bmp2tiff_wrapper.cpp",
      ],
      "include_dirs": [
        "../libtiff/libtiff/",
	"../gyp-zlib/zlib/",
	"../gyp-libjpeg/libjpeg",
		"../libtiff/port/",
		"../config/<(OS)/<(target_arch)",
      ],
    }
  ]
}
