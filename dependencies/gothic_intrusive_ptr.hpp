#pragma once

#include <ZenGin/zGothicAPI.h>
#include <crimson_cell/intrusive_ptr.hpp>

#if __G1
namespace Gothic_I_Classic
{
    // zCObject
    inline void intrusive_ptr_add_ref(zCObject* object) { object->AddRef(); }
    inline void intrusive_ptr_release(zCObject* object) { object->Release(); }

    // zCMenuItem
    inline void intrusive_ptr_add_ref(zCMenuItem* object) { ++object->m_iRefCtr; }
    inline void intrusive_ptr_release(zCMenuItem* object) { --object->m_iRefCtr; }

    // zCModelPrototype
    inline void intrusive_ptr_add_ref(zCModelPrototype* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCModelPrototype* object) { object->Release(); }

    // zCMorphMeshProto
    inline void intrusive_ptr_add_ref(zCMorphMeshProto* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCMorphMeshProto* object) { object->Release(); }

    // zCMusicJingle
    inline void intrusive_ptr_add_ref(zCMusicJingle* object) { object->AddRef(); }
    inline void intrusive_ptr_release(zCMusicJingle* object) { object->Release(); }

    // zCSndChannel
    inline void intrusive_ptr_add_ref(zCSndChannel* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCSndChannel* object) { --object->refCtr; }

    // zCWaveData
    inline void intrusive_ptr_add_ref(zCWaveData* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCWaveData* object) { object->Release(); }
}
#endif

#if __G1A
namespace Gothic_I_Addon
{
// zCObject
    inline void intrusive_ptr_add_ref(zCObject* object) { object->AddRef(); }
    inline void intrusive_ptr_release(zCObject* object) { object->Release(); }

    // zCMenuItem
    inline void intrusive_ptr_add_ref(zCMenuItem* object) { ++object->m_iRefCtr; }
    inline void intrusive_ptr_release(zCMenuItem* object) { --object->m_iRefCtr; }

    // zCModelPrototype
    inline void intrusive_ptr_add_ref(zCModelPrototype* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCModelPrototype* object) { object->Release(); }

    // zCMorphMeshProto
    inline void intrusive_ptr_add_ref(zCMorphMeshProto* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCMorphMeshProto* object) { object->Release(); }

    // zCMusicJingle
    inline void intrusive_ptr_add_ref(zCMusicJingle* object) { object->AddRef(); }
    inline void intrusive_ptr_release(zCMusicJingle* object) { object->Release(); }

    // zCSndChannel
    inline void intrusive_ptr_add_ref(zCSndChannel* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCSndChannel* object) { --object->refCtr; }

    // zCWaveData
    inline void intrusive_ptr_add_ref(zCWaveData* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCWaveData* object) { object->Release(); }
}
#endif

#if __G2
namespace Gothic_II_Classic
{
// zCObject
    inline void intrusive_ptr_add_ref(zCObject* object) { object->AddRef(); }
    inline void intrusive_ptr_release(zCObject* object) { object->Release(); }

    // zCMenuItem
    inline void intrusive_ptr_add_ref(zCMenuItem* object) { ++object->m_iRefCtr; }
    inline void intrusive_ptr_release(zCMenuItem* object) { object->Release(); }

    // zCModelPrototype
    inline void intrusive_ptr_add_ref(zCModelPrototype* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCModelPrototype* object) { object->Release(); }

    // zCMorphMeshProto
    inline void intrusive_ptr_add_ref(zCMorphMeshProto* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCMorphMeshProto* object) { object->Release(); }

    // zCMusicJingle
    inline void intrusive_ptr_add_ref(zCMusicJingle* object) { object->AddRef(); }
    inline void intrusive_ptr_release(zCMusicJingle* object) { object->Release(); }

    // zCSndChannel
    inline void intrusive_ptr_add_ref(zCSndChannel* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCSndChannel* object) { --object->refCtr; }

    // zCWaveData
    inline void intrusive_ptr_add_ref(zCWaveData* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCWaveData* object) { object->Release(); }
}
#endif

#if __G2A
namespace Gothic_II_Addon
{
    // zCObject
    inline void intrusive_ptr_add_ref(zCObject* object) { object->AddRef(); }
    inline void intrusive_ptr_release(zCObject* object) { object->Release(); }

    // zCMenuItem
    inline void intrusive_ptr_add_ref(zCMenuItem* object) { ++object->m_iRefCtr; }
    inline void intrusive_ptr_release(zCMenuItem* object) { object->Release(); }

    // zCModelPrototype
    inline void intrusive_ptr_add_ref(zCModelPrototype* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCModelPrototype* object) { object->Release(); }

    // zCMorphMeshProto
    inline void intrusive_ptr_add_ref(zCMorphMeshProto* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCMorphMeshProto* object) { object->Release(); }

    // zCMusicJingle
    inline void intrusive_ptr_add_ref(zCMusicJingle* object) { object->AddRef(); }
    inline void intrusive_ptr_release(zCMusicJingle* object) { object->Release(); }

    // zCSndChannel
    inline void intrusive_ptr_add_ref(zCSndChannel* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCSndChannel* object) { --object->refCtr; }

    // zCWaveData
    inline void intrusive_ptr_add_ref(zCWaveData* object) { ++object->refCtr; }
    inline void intrusive_ptr_release(zCWaveData* object) { object->Release(); }
}
#endif