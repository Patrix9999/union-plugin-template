#pragma once

#include <ZenGin/zGothicAPI.h>
#include <crimson_cell/intrusive_ptr.hpp>

#if __G1
namespace Gothic_I_Classic
{
    inline void intrusive_ptr_add_ref(zCObject* object) {
        object->AddRef();
    }

    inline void intrusive_ptr_release(zCObject* object) {
        object->Release();
    }
}
#endif

#if __G1A
namespace Gothic_I_Addon
{
    inline void intrusive_ptr_add_ref(zCObject* object) {
        object->AddRef();
    }

    inline void intrusive_ptr_release(zCObject* object) {
        object->Release();
    }
}
#endif

#if __G2
namespace Gothic_II_Classic
{
    inline void intrusive_ptr_add_ref(zCObject* object) {
        object->AddRef();
    }

    inline void intrusive_ptr_release(zCObject* object) {
        object->Release();
    }
}
#endif

#if __G2A
namespace Gothic_II_Addon
{
    inline void intrusive_ptr_add_ref(zCObject* object) {
        object->AddRef();
    }

    inline void intrusive_ptr_release(zCObject* object) {
        object->Release();
    }
}
#endif