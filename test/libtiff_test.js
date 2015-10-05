'use strict';
var libtiff = require('./build/Release/tiff_test');
var expect = require('chai').expect;

describe('functionality', function() {

    describe('bmp2tiff_test', function() {

        it('should be able to convert bmp images to tiff images', function() {
            var result = libtiff.bmp2tiff('palette-1c-8b.bmp', 'testimg.tiff');
            expect(result).to.eql(0);
        });
    });
});
