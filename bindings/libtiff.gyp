{
  'variables': { 'target_arch%': 'ia32' },

  'target_defaults': {
    'default_configuration': 'Debug',
    'configurations': {
      'Debug': {
        'defines': [ 'DEBUG', '_DEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 1, # static debug
          },
        },
      },
      'Release': {
        'defines': [ 'NDEBUG' ],
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 0, # static release
          },
        },
      }
    },
    'msvs_settings': {
      'VCLinkerTool': {
        'GenerateDebugInformation': 'true',
      },
    },
    'include_dirs': [
       # platform and arch-specific headers
       '../config/<(OS)/<(target_arch)'
     ],
  },

  "targets": [
        {
            "target_name": "libtiff",
	    #'product_prefix': 'lib',
            "type": "static_library",
            "include_dirs": [
                "../libtiff/libtiff/"
            ],
            "sources": [
             "../libtiff/libtiff/tif_aux.c",
  	     "../libtiff/libtiff/tif_close.c",
  	     "../libtiff/libtiff/tif_codec.c",
  	     "../libtiff/libtiff/tif_color.c",
  	     "../libtiff/libtiff/tif_compress.c",
  	     "../libtiff/libtiff/tif_dir.c",
             "../libtiff/libtiff/tif_dirinfo.c",
  	     "../libtiff/libtiff/tif_dirread.c",
  	     "../libtiff/libtiff/tif_dirwrite.c",
  	     "../libtiff/libtiff/tif_dumpmode.c",
    	     "../libtiff/libtiff/tif_error.c",
  	     "../libtiff/libtiff/tif_extension.c",
  	     "../libtiff/libtiff/tif_fax3.c",
  	     "../libtiff/libtiff/tif_fax3sm.c",
  	"../libtiff/libtiff/tif_flush.c",
  	"../libtiff/libtiff/tif_getimage.c",
 	 "../libtiff/libtiff/tif_jbig.c",
  	"../libtiff/libtiff/tif_jpeg.c",
  	"../libtiff/libtiff/tif_jpeg_12.c",
  	"../libtiff/libtiff/tif_luv.c",
  	"../libtiff/libtiff/tif_lzma.c",
  	"../libtiff/libtiff/tif_lzw.c",
  	"../libtiff/libtiff/tif_next.c",
  	"../libtiff/libtiff/tif_ojpeg.c",
  	"../libtiff/libtiff/tif_open.c",
 	 "../libtiff/libtiff/tif_packbits.c",
 	 "../libtiff/libtiff/tif_pixarlog.c",
  	"../libtiff/libtiff/tif_predict.c",
  	"../libtiff/libtiff/tif_print.c",
 	 "../libtiff/libtiff/tif_read.c",
  	"../libtiff/libtiff/tif_strip.c",
  	"../libtiff/libtiff/tif_swab.c",
  	"../libtiff/libtiff/tif_thunder.c",
  	"../libtiff/libtiff/tif_tile.c",
  	"../libtiff/libtiff/tif_version.c",
  	"../libtiff/libtiff/tif_warning.c",
  	"../libtiff/libtiff/tif_write.c",
  	"../libtiff/libtiff/tif_zip.c",
            ],
            "conditions": [
                [
                    "OS==\"linux\"",
                    {
                        "defines": [
                            "STDC_HEADERS"
            		],
                    }
                ],
                [
                    "OS==\"mac\"",
                    {
                        "defines": [
                            #"USE_MAC_MEMMGR"
                        ],
                        "include_dirs": [
                            "platform-includes/mac/libjpeg"
                        ],
                        "sources" : [
                            #"../libjpeg/jmemmac.c"
                        ]
                    }
                ],
                [
                    "OS==\"win\"",
                    {
                        "defines": [
                            #"USE_MSDOS_MEMMGR",
                            "MSDOS"
                        ],
                        "include_dirs": [
                            "platform-includes/win/libjpeg"
                        ],
                        "sources" : [
                            #"../libjpeg/jmemdos.c"
                        ],
                    }
                ]
            ]
        }
    ]
}
