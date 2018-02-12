#!/usr/bin/env python2
## -*- coding: utf-8 -*-

import sys

def sx(bits, value):
    sign_bit = 1 << (bits - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

SymVar_0 = int(sys.argv[1])
ref_214 = SymVar_0
ref_225 = ref_214 # MOV operation
ref_237 = ref_225 # MOV operation
ref_239 = ref_237 # MOV operation
ref_108418 = ref_239 # MOV operation
ref_108462 = ref_108418 # MOV operation
ref_108497 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_108462) # MOV operation
ref_108538 = (((((((((0x7B) << 8 | 0x6B) << 8 | 0x69) << 8 | 0x6E) << 8 | 0x72) << 8 | 0x7E) << 8 | 0x6C) << 8 | 0x7B) ^ ref_108462) # MOV operation
ref_108540 = rol(0x10, ref_108538) # ROL operation
ref_108544 = (ref_108540 ^ ((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108591 = ref_108544 # MOV operation
ref_108615 = (0x96C62826CF6DE04E ^ ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108632 = ref_108544 # MOV operation
ref_108634 = rol(0x15, ref_108632) # ROL operation
ref_108638 = (ref_108634 ^ ((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108667 = ref_108615 # MOV operation
ref_108685 = ref_108638 # MOV operation
ref_108703 = ref_108615 # MOV operation
ref_108705 = rol(0xD, ref_108703) # ROL operation
ref_108709 = (ref_108705 ^ ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108726 = ref_108638 # MOV operation
ref_108728 = rol(0x10, ref_108726) # ROL operation
ref_108732 = (ref_108728 ^ ((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108761 = ref_108709 # MOV operation
ref_108779 = ref_108732 # MOV operation
ref_108797 = ref_108709 # MOV operation
ref_108799 = rol(0x11, ref_108797) # ROL operation
ref_108803 = (ref_108799 ^ ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF) + ref_108761) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108820 = ref_108732 # MOV operation
ref_108822 = rol(0x15, ref_108820) # ROL operation
ref_108826 = (ref_108822 ^ ((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) + ref_108779) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_108855 = ref_108418 # MOV operation
ref_108979 = ref_108803 # MOV operation
ref_108997 = (ref_108826 ^ 0x800000000000000) # MOV operation
ref_109015 = ref_108803 # MOV operation
ref_109017 = rol(0xD, ref_109015) # ROL operation
ref_109021 = (ref_109017 ^ (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) + ref_108779) & 0xFFFFFFFFFFFFFFFF) ^ ref_108855) + ref_108979) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109038 = (ref_108826 ^ 0x800000000000000) # MOV operation
ref_109040 = rol(0x10, ref_109038) # ROL operation
ref_109044 = (ref_109040 ^ ((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF) + ref_108761) & 0xFFFFFFFFFFFFFFFF)) + ref_108997) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109073 = ref_109021 # MOV operation
ref_109091 = ref_109044 # MOV operation
ref_109109 = ref_109021 # MOV operation
ref_109111 = rol(0x11, ref_109109) # ROL operation
ref_109115 = (ref_109111 ^ ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF) + ref_108761) & 0xFFFFFFFFFFFFFFFF)) + ref_108997) & 0xFFFFFFFFFFFFFFFF) + ref_109073) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109132 = ref_109044 # MOV operation
ref_109134 = rol(0x15, ref_109132) # ROL operation
ref_109138 = (ref_109134 ^ ((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) + ref_108779) & 0xFFFFFFFFFFFFFFFF) ^ ref_108855) + ref_108979) & 0xFFFFFFFFFFFFFFFF)) + ref_109091) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109167 = ref_109115 # MOV operation
ref_109185 = ref_109138 # MOV operation
ref_109203 = ref_109115 # MOV operation
ref_109205 = rol(0xD, ref_109203) # ROL operation
ref_109209 = (ref_109205 ^ ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) + ref_108779) & 0xFFFFFFFFFFFFFFFF) ^ ref_108855) + ref_108979) & 0xFFFFFFFFFFFFFFFF)) + ref_109091) & 0xFFFFFFFFFFFFFFFF) + ref_109167) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109226 = ref_109138 # MOV operation
ref_109228 = rol(0x10, ref_109226) # ROL operation
ref_109232 = (ref_109228 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF) + ref_108761) & 0xFFFFFFFFFFFFFFFF)) + ref_108997) & 0xFFFFFFFFFFFFFFFF) + ref_109073) & 0xFFFFFFFFFFFFFFFF)) + ref_109185) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109261 = ref_109209 # MOV operation
ref_109279 = ref_109232 # MOV operation
ref_109297 = ref_109209 # MOV operation
ref_109299 = rol(0x11, ref_109297) # ROL operation
ref_109303 = (ref_109299 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF) + ref_108761) & 0xFFFFFFFFFFFFFFFF)) + ref_108997) & 0xFFFFFFFFFFFFFFFF) + ref_109073) & 0xFFFFFFFFFFFFFFFF)) + ref_109185) & 0xFFFFFFFFFFFFFFFF) + ref_109261) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109320 = ref_109232 # MOV operation
ref_109322 = rol(0x15, ref_109320) # ROL operation
ref_109326 = (ref_109322 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) + ref_108779) & 0xFFFFFFFFFFFFFFFF) ^ ref_108855) + ref_108979) & 0xFFFFFFFFFFFFFFFF)) + ref_109091) & 0xFFFFFFFFFFFFFFFF) + ref_109167) & 0xFFFFFFFFFFFFFFFF)) + ref_109279) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109387 = ref_109303 # MOV operation
ref_109405 = ref_109326 # MOV operation
ref_109423 = ref_109303 # MOV operation
ref_109425 = rol(0xD, ref_109423) # ROL operation
ref_109429 = (ref_109425 ^ (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) + ref_108779) & 0xFFFFFFFFFFFFFFFF) ^ ref_108855) + ref_108979) & 0xFFFFFFFFFFFFFFFF)) + ref_109091) & 0xFFFFFFFFFFFFFFFF) + ref_109167) & 0xFFFFFFFFFFFFFFFF)) + ref_109279) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_109387) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109446 = ref_109326 # MOV operation
ref_109448 = rol(0x10, ref_109446) # ROL operation
ref_109452 = (ref_109448 ^ (((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF) + ref_108761) & 0xFFFFFFFFFFFFFFFF)) + ref_108997) & 0xFFFFFFFFFFFFFFFF) + ref_109073) & 0xFFFFFFFFFFFFFFFF)) + ref_109185) & 0xFFFFFFFFFFFFFFFF) + ref_109261) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_109405) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109481 = ref_109429 # MOV operation
ref_109499 = ref_109452 # MOV operation
ref_109517 = ref_109429 # MOV operation
ref_109519 = rol(0x11, ref_109517) # ROL operation
ref_109523 = (ref_109519 ^ (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF) + ref_108761) & 0xFFFFFFFFFFFFFFFF)) + ref_108997) & 0xFFFFFFFFFFFFFFFF) + ref_109073) & 0xFFFFFFFFFFFFFFFF)) + ref_109185) & 0xFFFFFFFFFFFFFFFF) + ref_109261) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_109405) & 0xFFFFFFFFFFFFFFFF) + ref_109481) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109540 = ref_109452 # MOV operation
ref_109542 = rol(0x15, ref_109540) # ROL operation
ref_109546 = (ref_109542 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) + ref_108779) & 0xFFFFFFFFFFFFFFFF) ^ ref_108855) + ref_108979) & 0xFFFFFFFFFFFFFFFF)) + ref_109091) & 0xFFFFFFFFFFFFFFFF) + ref_109167) & 0xFFFFFFFFFFFFFFFF)) + ref_109279) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_109387) & 0xFFFFFFFFFFFFFFFF)) + ref_109499) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109575 = ref_109523 # MOV operation
ref_109593 = ref_109546 # MOV operation
ref_109611 = ref_109523 # MOV operation
ref_109613 = rol(0xD, ref_109611) # ROL operation
ref_109617 = (ref_109613 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) + ref_108779) & 0xFFFFFFFFFFFFFFFF) ^ ref_108855) + ref_108979) & 0xFFFFFFFFFFFFFFFF)) + ref_109091) & 0xFFFFFFFFFFFFFFFF) + ref_109167) & 0xFFFFFFFFFFFFFFFF)) + ref_109279) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_109387) & 0xFFFFFFFFFFFFFFFF)) + ref_109499) & 0xFFFFFFFFFFFFFFFF) + ref_109575) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109634 = ref_109546 # MOV operation
ref_109636 = rol(0x10, ref_109634) # ROL operation
ref_109640 = (ref_109636 ^ ((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF) + ref_108761) & 0xFFFFFFFFFFFFFFFF)) + ref_108997) & 0xFFFFFFFFFFFFFFFF) + ref_109073) & 0xFFFFFFFFFFFFFFFF)) + ref_109185) & 0xFFFFFFFFFFFFFFFF) + ref_109261) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_109405) & 0xFFFFFFFFFFFFFFFF) + ref_109481) & 0xFFFFFFFFFFFFFFFF)) + ref_109593) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109669 = ref_109617 # MOV operation
ref_109687 = ref_109640 # MOV operation
ref_109705 = ref_109617 # MOV operation
ref_109707 = rol(0x11, ref_109705) # ROL operation
ref_109711 = (ref_109707 ^ ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF) + ref_108761) & 0xFFFFFFFFFFFFFFFF)) + ref_108997) & 0xFFFFFFFFFFFFFFFF) + ref_109073) & 0xFFFFFFFFFFFFFFFF)) + ref_109185) & 0xFFFFFFFFFFFFFFFF) + ref_109261) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_109405) & 0xFFFFFFFFFFFFFFFF) + ref_109481) & 0xFFFFFFFFFFFFFFFF)) + ref_109593) & 0xFFFFFFFFFFFFFFFF) + ref_109669) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109728 = ref_109640 # MOV operation
ref_109730 = rol(0x15, ref_109728) # ROL operation
ref_109734 = (ref_109730 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) + ref_108779) & 0xFFFFFFFFFFFFFFFF) ^ ref_108855) + ref_108979) & 0xFFFFFFFFFFFFFFFF)) + ref_109091) & 0xFFFFFFFFFFFFFFFF) + ref_109167) & 0xFFFFFFFFFFFFFFFF)) + ref_109279) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_109387) & 0xFFFFFFFFFFFFFFFF)) + ref_109499) & 0xFFFFFFFFFFFFFFFF) + ref_109575) & 0xFFFFFFFFFFFFFFFF)) + ref_109687) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109763 = ref_109711 # MOV operation
ref_109781 = ref_109734 # MOV operation
ref_109799 = ref_109711 # MOV operation
ref_109801 = rol(0xD, ref_109799) # ROL operation
ref_109805 = (ref_109801 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) + ref_108779) & 0xFFFFFFFFFFFFFFFF) ^ ref_108855) + ref_108979) & 0xFFFFFFFFFFFFFFFF)) + ref_109091) & 0xFFFFFFFFFFFFFFFF) + ref_109167) & 0xFFFFFFFFFFFFFFFF)) + ref_109279) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_109387) & 0xFFFFFFFFFFFFFFFF)) + ref_109499) & 0xFFFFFFFFFFFFFFFF) + ref_109575) & 0xFFFFFFFFFFFFFFFF)) + ref_109687) & 0xFFFFFFFFFFFFFFFF) + ref_109763) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109822 = ref_109734 # MOV operation
ref_109824 = rol(0x10, ref_109822) # ROL operation
ref_109828 = (ref_109824 ^ ((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF) + ref_108761) & 0xFFFFFFFFFFFFFFFF)) + ref_108997) & 0xFFFFFFFFFFFFFFFF) + ref_109073) & 0xFFFFFFFFFFFFFFFF)) + ref_109185) & 0xFFFFFFFFFFFFFFFF) + ref_109261) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_109405) & 0xFFFFFFFFFFFFFFFF) + ref_109481) & 0xFFFFFFFFFFFFFFFF)) + ref_109593) & 0xFFFFFFFFFFFFFFFF) + ref_109669) & 0xFFFFFFFFFFFFFFFF)) + ref_109781) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109857 = ref_109805 # MOV operation
ref_109875 = ref_109828 # MOV operation
ref_109893 = ref_109805 # MOV operation
ref_109895 = rol(0x11, ref_109893) # ROL operation
ref_109899 = (ref_109895 ^ ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF) + ref_108761) & 0xFFFFFFFFFFFFFFFF)) + ref_108997) & 0xFFFFFFFFFFFFFFFF) + ref_109073) & 0xFFFFFFFFFFFFFFFF)) + ref_109185) & 0xFFFFFFFFFFFFFFFF) + ref_109261) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_109405) & 0xFFFFFFFFFFFFFFFF) + ref_109481) & 0xFFFFFFFFFFFFFFFF)) + ref_109593) & 0xFFFFFFFFFFFFFFFF) + ref_109669) & 0xFFFFFFFFFFFFFFFF)) + ref_109781) & 0xFFFFFFFFFFFFFFFF) + ref_109857) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109916 = ref_109828 # MOV operation
ref_109918 = rol(0x15, ref_109916) # ROL operation
ref_109922 = (ref_109918 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) + ref_108779) & 0xFFFFFFFFFFFFFFFF) ^ ref_108855) + ref_108979) & 0xFFFFFFFFFFFFFFFF)) + ref_109091) & 0xFFFFFFFFFFFFFFFF) + ref_109167) & 0xFFFFFFFFFFFFFFFF)) + ref_109279) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_109387) & 0xFFFFFFFFFFFFFFFF)) + ref_109499) & 0xFFFFFFFFFFFFFFFF) + ref_109575) & 0xFFFFFFFFFFFFFFFF)) + ref_109687) & 0xFFFFFFFFFFFFFFFF) + ref_109763) & 0xFFFFFFFFFFFFFFFF)) + ref_109875) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_109951 = ref_109899 # MOV operation
ref_109969 = ref_109922 # MOV operation
ref_109987 = ref_109899 # MOV operation
ref_109989 = rol(0xD, ref_109987) # ROL operation
ref_109993 = (ref_109989 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) + ref_108779) & 0xFFFFFFFFFFFFFFFF) ^ ref_108855) + ref_108979) & 0xFFFFFFFFFFFFFFFF)) + ref_109091) & 0xFFFFFFFFFFFFFFFF) + ref_109167) & 0xFFFFFFFFFFFFFFFF)) + ref_109279) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_109387) & 0xFFFFFFFFFFFFFFFF)) + ref_109499) & 0xFFFFFFFFFFFFFFFF) + ref_109575) & 0xFFFFFFFFFFFFFFFF)) + ref_109687) & 0xFFFFFFFFFFFFFFFF) + ref_109763) & 0xFFFFFFFFFFFFFFFF)) + ref_109875) & 0xFFFFFFFFFFFFFFFF) + ref_109951) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_110010 = ref_109922 # MOV operation
ref_110012 = rol(0x10, ref_110010) # ROL operation
ref_110016 = (ref_110012 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF) + ref_108761) & 0xFFFFFFFFFFFFFFFF)) + ref_108997) & 0xFFFFFFFFFFFFFFFF) + ref_109073) & 0xFFFFFFFFFFFFFFFF)) + ref_109185) & 0xFFFFFFFFFFFFFFFF) + ref_109261) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_109405) & 0xFFFFFFFFFFFFFFFF) + ref_109481) & 0xFFFFFFFFFFFFFFFF)) + ref_109593) & 0xFFFFFFFFFFFFFFFF) + ref_109669) & 0xFFFFFFFFFFFFFFFF)) + ref_109781) & 0xFFFFFFFFFFFFFFFF) + ref_109857) & 0xFFFFFFFFFFFFFFFF)) + ref_109969) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_110045 = ref_109993 # MOV operation
ref_110063 = ref_110016 # MOV operation
ref_110081 = ref_109993 # MOV operation
ref_110083 = rol(0x11, ref_110081) # ROL operation
ref_110087 = (ref_110083 ^ ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF) + ref_108761) & 0xFFFFFFFFFFFFFFFF)) + ref_108997) & 0xFFFFFFFFFFFFFFFF) + ref_109073) & 0xFFFFFFFFFFFFFFFF)) + ref_109185) & 0xFFFFFFFFFFFFFFFF) + ref_109261) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_109405) & 0xFFFFFFFFFFFFFFFF) + ref_109481) & 0xFFFFFFFFFFFFFFFF)) + ref_109593) & 0xFFFFFFFFFFFFFFFF) + ref_109669) & 0xFFFFFFFFFFFFFFFF)) + ref_109781) & 0xFFFFFFFFFFFFFFFF) + ref_109857) & 0xFFFFFFFFFFFFFFFF)) + ref_109969) & 0xFFFFFFFFFFFFFFFF) + ref_110045) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_110104 = ref_110016 # MOV operation
ref_110106 = rol(0x15, ref_110104) # ROL operation
ref_110110 = (ref_110106 ^ ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) + ref_108779) & 0xFFFFFFFFFFFFFFFF) ^ ref_108855) + ref_108979) & 0xFFFFFFFFFFFFFFFF)) + ref_109091) & 0xFFFFFFFFFFFFFFFF) + ref_109167) & 0xFFFFFFFFFFFFFFFF)) + ref_109279) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_109387) & 0xFFFFFFFFFFFFFFFF)) + ref_109499) & 0xFFFFFFFFFFFFFFFF) + ref_109575) & 0xFFFFFFFFFFFFFFFF)) + ref_109687) & 0xFFFFFFFFFFFFFFFF) + ref_109763) & 0xFFFFFFFFFFFFFFFF)) + ref_109875) & 0xFFFFFFFFFFFFFFFF) + ref_109951) & 0xFFFFFFFFFFFFFFFF)) + ref_110063) & 0xFFFFFFFFFFFFFFFF)) # XOR operation
ref_110139 = ((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((((((((((0xD8) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xDA) << 8 | 0xDF) << 8 | 0xCA) << 8 | 0xE7) << 8 | 0xCE) + ref_108591) & 0xFFFFFFFFFFFFFFFF) + ref_108667) & 0xFFFFFFFFFFFFFFFF)) + ref_108779) & 0xFFFFFFFFFFFFFFFF) ^ ref_108855) + ref_108979) & 0xFFFFFFFFFFFFFFFF)) + ref_109091) & 0xFFFFFFFFFFFFFFFF) + ref_109167) & 0xFFFFFFFFFFFFFFFF)) + ref_109279) & 0xFFFFFFFFFFFFFFFF) ^ 0x800000000000000) + ref_109387) & 0xFFFFFFFFFFFFFFFF)) + ref_109499) & 0xFFFFFFFFFFFFFFFF) + ref_109575) & 0xFFFFFFFFFFFFFFFF)) + ref_109687) & 0xFFFFFFFFFFFFFFFF) + ref_109763) & 0xFFFFFFFFFFFFFFFF)) + ref_109875) & 0xFFFFFFFFFFFFFFFF) + ref_109951) & 0xFFFFFFFFFFFFFFFF)) + ref_110063) & 0xFFFFFFFFFFFFFFFF) # MOV operation
ref_110141 = (ref_110139 ^ ref_110087) # XOR operation
ref_110148 = ref_110141 # MOV operation
ref_110150 = rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, (((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((rol(0x20, ((((((((((((0x6B) << 8 | 0x7F) << 8 | 0x62) << 8 | 0x61) << 8 | 0x6D) << 8 | 0x67) << 8 | 0x73) << 8 | 0x61) + ref_108497) & 0xFFFFFFFFFFFFFFFF) + 0xF0274B63141367B6) & 0xFFFFFFFFFFFFFFFF)) + ref_108685) & 0xFFFFFFFFFFFFFFFF) + ref_108761) & 0xFFFFFFFFFFFFFFFF)) + ref_108997) & 0xFFFFFFFFFFFFFFFF) + ref_109073) & 0xFFFFFFFFFFFFFFFF)) + ref_109185) & 0xFFFFFFFFFFFFFFFF) + ref_109261) & 0xFFFFFFFFFFFFFFFF)) ^ 0xFF) + ref_109405) & 0xFFFFFFFFFFFFFFFF) + ref_109481) & 0xFFFFFFFFFFFFFFFF)) + ref_109593) & 0xFFFFFFFFFFFFFFFF) + ref_109669) & 0xFFFFFFFFFFFFFFFF)) + ref_109781) & 0xFFFFFFFFFFFFFFFF) + ref_109857) & 0xFFFFFFFFFFFFFFFF)) + ref_109969) & 0xFFFFFFFFFFFFFFFF) + ref_110045) & 0xFFFFFFFFFFFFFFFF)) # MOV operation
ref_110152 = (ref_110150 ^ ref_110110) # XOR operation
ref_110159 = (ref_110152 ^ ref_110148) # XOR operation
ref_111408 = ref_110159 # MOV operation
ref_112165 = ref_111408 # MOV operation
ref_113400 = ref_112165 # MOV operation
ref_114197 = ref_113400 # MOV operation
ref_114235 = ref_114197 # MOV operation
ref_114247 = ref_114235 # MOV operation
ref_114249 = ref_114247 # MOV operation

print ref_114249 & 0xffffffffffffffff