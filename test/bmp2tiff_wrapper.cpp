#include <iostream>
#include <node.h>
#include <v8.h>

using namespace std;
using namespace v8;

extern "C" int bmp2tiff_main(int argc, char* argv[]);

void bmp2tiff(const FunctionCallbackInfo<v8::Value>& args)
{
	v8::Isolate* isolate;
	isolate = args.GetIsolate();
	int argc = 3;
	char* argv[] = {"bmp2tiff", "palette-1c-8b.bmp", "test.tiff"};
	
	int status = bmp2tiff_main(argc, argv);
	Local<Number> out = Number::New(isolate, status);
	args.GetReturnValue().Set(out);
	return;
}

void init(Handle<Object> exports) 
{
  Isolate* isolate = v8::Isolate::GetCurrent();
  exports->Set(String::NewFromUtf8(isolate, "bmp2tiff", v8::String::kInternalizedString),
      FunctionTemplate::New(isolate, bmp2tiff)->GetFunction());
}
 
NODE_MODULE(tiff_test, init)