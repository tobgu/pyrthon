from pyrthon._transformer import PyrsistentTransformer

def load_ipython_extension(ipython):
    ''' load extension for prython in ipython'''
    pyr_transform = PyrsistentTransformer()
    ipython.ast_transformers.append(pyr_transform)
    print("'pyrthon' extension loaded ")

def unload_ipython_extension(ipython):
    ''' unload the pyrthon ipython extension'''
    ipython.ast_transformers = [transformer 
            for transformer in ipython.ast_transformers 
            if not isinstance(transformer, PyrsistentTransformer)]
    print("'pyrthon' extension unloaded")
