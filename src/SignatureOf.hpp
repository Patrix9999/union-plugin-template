#pragma once

#ifdef __G1
#include "g1_signatures.hpp"
#endif

#ifdef __G1A
#include "g1a_signatures.hpp"
#endif

#ifdef __G2
#include "g2_signatures.hpp"
#endif

#ifdef __G2A
#include "g2a_signatures.hpp"
#endif

#undef SIGNATURE_OF

#if __G1 && __G1A && __G2 && __G2A
#define SIGNATURE_OF(what) reinterpret_cast<void*>(zSwitch(Gothic_I_Classic::SignatureToAddress(#what), Gothic_I_Addon::SignatureToAddress(#what), Gothic_II_Classic::SignatureToAddress(#what), Gothic_II_Addon::SignatureToAddress(#what)))
#elif __G1
#define SIGNATURE_OF(what) reinterpret_cast<void*>(Gothic_I_Classic::SignatureToAddress(#what))
#elif __G1A
#define SIGNATURE_OF(what) reinterpret_cast<void*>(Gothic_I_Addon::SignatureToAddress(#what))
#elif __G2
#define SIGNATURE_OF(what) reinterpret_cast<void*>(Gothic_II_Classic::SignatureToAddress(#what))
#elif __G2A
#define SIGNATURE_OF(what) reinterpret_cast<void*>(Gothic_II_Addon::SignatureToAddress(#what))
#endif
