#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Volibear_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin9.bin"
    "DATA/Characters/Volibear/Volibear.bin"
    "DATA/Characters/Volibear/Animations/Skin0.bin"
    "DATA/Volibear_Skins_Root_Skins_Skin0_Skins_Skin19_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28.bin"
    "DATA/Volibear_Skins_Skin19_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28.bin"
}
entries: map[hash,embed] = {
    0xa8a2f582 = SkinCharacterDataProperties {
        skinClassification: u32 = 2
        championSkinName: string = "VolibearSkin21"
        skinParent: i32 = 19
        metaDataTags: string = "faction:freljord,gender:male,element:lightning,race:demigod,skinline:inkshadow"
        skinUpgradeData: embed = skinUpgradeData {
            0xcb522723: list[link] = {
                0xe555b8a9
                0xddf1fc08
                0x2b2f6a75
                0xffa3e44c
            }
        }
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Characters/Volibear/Skins/Skin19/VolibearLoadScreen_19.tex"
        }
        loadscreenVintage: embed = CensoredImage {
            image: string = "ASSETS/Characters/Volibear/Skins/Skin19/VolibearLoadScreen_19_LE.tex"
        }
        skinAudioProperties: embed = skinAudioProperties {
            tagEventList: list[string] = {
                "Volibear"
            }
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "Volibear_Base_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Volibear/Skins/Base/Volibear_Base_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Volibear/Skins/Base/Volibear_Base_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_Volibear_Celebrate_buffactivate"
                        "Play_sfx_Volibear_Dance3D_buffactivate"
                        "Play_sfx_Volibear_Dance3D_loop"
                        "Play_sfx_Volibear_Death3D_cast"
                        "Play_sfx_Volibear_Joke3D_buffactivate"
                        "Play_sfx_Volibear_Joke3D_loop"
                        "Play_sfx_Volibear_Laugh3D_buffactivate"
                        "Play_sfx_Volibear_Recall3D_buffactivate"
                        "Play_sfx_Volibear_Respawn3D_buffactivate"
                        "Play_sfx_Volibear_Roar_cast"
                        "Play_sfx_Volibear_StartRun_loop"
                        "Play_sfx_Volibear_Taunt3D_buffactivate"
                        "Play_sfx_Volibear_VolibearBasicAttack_OnCast"
                        "Play_sfx_Volibear_VolibearBasicAttack_OnHit"
                        "Play_sfx_Volibear_VolibearBasicAttackTower_OnCast"
                        "Play_sfx_Volibear_VolibearBasicAttackTower_OnHit"
                        "Play_sfx_Volibear_VolibearCritAttack_OnCast"
                        "Play_sfx_Volibear_VolibearCritAttack_OnHit"
                        "Play_sfx_Volibear_VolibearE_buffactivate"
                        "Play_sfx_Volibear_VolibearE_enemy_buffactivate"
                        "Play_sfx_Volibear_VolibearE_explo"
                        "Play_sfx_Volibear_VolibearE_hit"
                        "Play_sfx_Volibear_VolibearE_OnCast"
                        "Play_sfx_Volibear_VolibearEShield_OnBuffActivate"
                        "Play_sfx_Volibear_VolibearEShield_OnBuffDeactivate"
                        "Play_sfx_Volibear_VolibearPApplicator_OnBuffActivate"
                        "Play_sfx_Volibear_VolibearPApplicator_OnBuffDeactivate"
                        "Play_sfx_Volibear_VolibearPChain_hit"
                        "Play_sfx_Volibear_VolibearQ_footsteps"
                        "Play_sfx_Volibear_VolibearQ_OnBuffActivate"
                        "Play_sfx_Volibear_VolibearQ_OnBuffDeactivate"
                        "Play_sfx_Volibear_VolibearQ_OnCast"
                        "Play_sfx_Volibear_VolibearQ_reset_others"
                        "Play_sfx_Volibear_VolibearQ_reset_self"
                        "Play_sfx_Volibear_VolibearQAttack_OnCast"
                        "Play_sfx_Volibear_VolibearQAttack_OnHit"
                        "Play_sfx_Volibear_VolibearQPostAttack_OnCast"
                        "Play_sfx_Volibear_VolibearQPostAttack_OnHit"
                        "Play_sfx_Volibear_VolibearR_buffactive_self"
                        "Play_sfx_Volibear_VolibearR_buffdeactive_self"
                        "Play_sfx_Volibear_VolibearR_cast"
                        "Play_sfx_Volibear_VolibearR_hit_ground"
                        "Play_sfx_Volibear_VolibearR_jump"
                        "Play_sfx_Volibear_VolibearR_OnBuffActivate"
                        "Play_sfx_Volibear_VolibearR_OnBuffDeactivate"
                        "Play_sfx_Volibear_VolibearRSweetSpot_hit"
                        "Play_sfx_Volibear_VolibearRSweetSpot_minion_hit"
                        "Play_sfx_Volibear_VolibearRTowerAttack1_OnCast"
                        "Play_sfx_Volibear_VolibearRTowerAttack1_OnHit"
                        "Play_sfx_Volibear_VolibearRTowerAttack2_OnCast"
                        "Play_sfx_Volibear_VolibearRTowerAttack2_OnHit"
                        "Play_sfx_Volibear_VolibearRTowerDisable_buffactive"
                        "Play_sfx_Volibear_VolibearRTowerDisable_hit"
                        "Play_sfx_Volibear_VolibearRTransitionAttack_OnCast"
                        "Play_sfx_Volibear_VolibearRTransitionAttack_OnHit"
                        "Play_sfx_Volibear_VolibearW_cast"
                        "Play_sfx_Volibear_VolibearW_hit"
                        "Play_sfx_Volibear_VolibearWEmp_cast"
                        "Play_sfx_Volibear_VolibearWEmp_hit"
                        "Play_sfx_Volibear_Winddown3D_buffactivate"
                        "Stop_sfx_Volibear_VolibearEShield_OnBuffActivate"
                        "Stop_sfx_Volibear_VolibearRTowerDisable_buffactive"
                    }
                }
                BankUnit {
                    name: string = "Volibear_Base_VO"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Volibear/Skins/Base/Volibear_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Volibear/Skins/Base/Volibear_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Volibear/Skins/Base/Volibear_Base_VO_audio.wpk"
                    }
                    events: list[string] = {
                        "Play_vo_Volibear_Attack2DGeneral"
                        "Play_vo_Volibear_Attack2DHuman"
                        "Play_vo_Volibear_Dance3DGeneral"
                        "Play_vo_Volibear_Death3D"
                        "Play_vo_Volibear_FirstEncounter3DAnivia"
                        "Play_vo_Volibear_FirstEncounter3DAshe"
                        "Play_vo_Volibear_FirstEncounter3DBraum"
                        "Play_vo_Volibear_FirstEncounter3DGeneral"
                        "Play_vo_Volibear_FirstEncounter3DHuman"
                        "Play_vo_Volibear_FirstEncounter3DLissandra"
                        "Play_vo_Volibear_FirstEncounter3DNunu"
                        "Play_vo_Volibear_FirstEncounter3DOrnn"
                        "Play_vo_Volibear_FirstEncounter3DRengar"
                        "Play_vo_Volibear_FirstEncounter3DSejuani"
                        "Play_vo_Volibear_FirstEncounter3DTryndamere"
                        "Play_vo_Volibear_FirstEncounter3DYuumi"
                        "Play_vo_Volibear_FirstEncounter3DZilean"
                        "Play_vo_Volibear_Idle3DGeneral"
                        "Play_vo_Volibear_Joke3DGeneral"
                        "Play_vo_Volibear_Kill3DAnivia"
                        "Play_vo_Volibear_Kill3DGeneral"
                        "Play_vo_Volibear_Kill3DHuman"
                        "Play_vo_Volibear_Kill3DOrnn"
                        "Play_vo_Volibear_Kill3DTurret"
                        "Play_vo_Volibear_Laugh3DGeneral"
                        "Play_vo_Volibear_Move2DFirst"
                        "Play_vo_Volibear_Move2DLong"
                        "Play_vo_Volibear_Move2DStandard"
                        "Play_vo_Volibear_Recall3DGeneral"
                        "Play_vo_Volibear_Respawn2DGeneral"
                        "Play_vo_Volibear_Taunt3DGeneral"
                        "Play_vo_Volibear_TauntResponse3DGeneral"
                        "Play_vo_Volibear_VolibearBasicAttack2_cast3D"
                        "Play_vo_Volibear_VolibearBasicAttack3_cast3D"
                        "Play_vo_Volibear_VolibearBasicAttack_cast3D"
                        "Play_vo_Volibear_VolibearCritAttack_cast3D"
                        "Play_vo_Volibear_VolibearE_cast3D"
                        "Play_vo_Volibear_VolibearQ_cast3D"
                        "Play_vo_Volibear_VolibearR_cast3D"
                        "Play_vo_Volibear_VolibearW_cast3D"
                    }
                    voiceOver: bool = true
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Volibear/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Volibear/Skins/Base/Volibear_Base.skl"
            simpleSkin: string = "ASSETS/Characters/Volibear/Skins/Base/Volibear_Base.skn"
            texture: string = "ASSETS/Characters/Volibear/Skins/Base/Volibear_Base_TX_CM.dds"
	 	 	skinScale: f32 = 2
            selfIllumination: f32 = 0.699999988
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            initialSubmeshToHide: string = "HeadFrenzy, FrenzyDaggers, ShacklePieces, Crystal, ShackleBlades"
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Volibear/Skins/Base/Volibear_Base_Ice_TX_CM.dds"
                    submesh: string = "ice_back"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Volibear/Skins/Base/Volibear_Base_Ice_TX_CM.dds"
                    submesh: string = "ice_legs"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Volibear/Skins/Base/Volibear_Base_Ice_TX_CM.dds"
                    submesh: string = "ice_arms"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Volibear/Skins/Base/Volibear_Base_Ice_TX_CM.dds"
                    submesh: string = "ice_arms_float"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Volibear/Skins/Base/Volibear_Base_Poro_TX_CM.dds"
                    submesh: string = "Poro"
                }
            }
        }
        armorMaterial: string = "Flesh"
        defaultAnimations: list[string] = {
            ""
        }
        mContextualActionData: link = "Characters/Volibear/CAC/Volibear_Base"
        iconCircle: option[string] = {
            "ASSETS/Characters/Volibear/HUD/Volibear_Circle_0.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Volibear/HUD/Volibear_Square.tex"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            attachToBone: string = "Buffbone_Cstm_Healthbar"
            unitHealthBarStyle: u8 = 12
        }
        mResourceResolver: link = "Characters/Volibear/Skins/Skin0/Resources"
    }
    0x082d55c5 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 3.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh"
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0xde5b1cd9: flag = true
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Shuriken.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 900
                alphaRef: u8 = 0
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 4, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 1.20000005, 0 }
                            { 0, 24, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.29999995, 5, 5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin21/Volibear_Skin21_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 3.5
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "backBlend"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.219607845, 0.0235294122, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 797
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 45, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 3.5
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "backBlend1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.764705896, 0.0549019612, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 798
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 45, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 3.5
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "backBlend2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.521568656, 0.129411772, 1 }
                }
                pass: i16 = 797
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 45, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                lifetime: option[f32] = {
                    3.4000001
                }
                emitterName: string = "Basic"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 50, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    flags: u8 = 1
                    0x23a0d95c: vec3 = { 30, 0, 30 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.113725491, 0.0156862754, 0, 0 }
                            { 0.113725491, 0.0156862754, 0, 0.568627477 }
                            { 0.0784313753, 0.00784313772, 0, 1 }
                            { 0.0901960805, 0.0117647061, 0, 0 }
                        }
                    }
                }
                pass: i16 = 796
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.200000003
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Z_Splats_02_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 40, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 40, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_BasicAttack_Splats_02.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                numFrames: u16 = 6
                startFrame: u16 = 1
                texDiv: vec2 = { 4, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                lifetime: option[f32] = {
                    3.5
                }
                emitterName: string = "Ink"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 4, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    flags: u8 = 1
                    0x23a0d95c: vec3 = { 30, 0, 30 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.113725491, 0.0156862754, 0, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.662745118, 1, 0.152941182, 0 }
                            { 0.65882355, 1, 0.20784314, 1 }
                            { 0.0784313753, 0.117647059, 0.0313725509, 1 }
                            { 0.0823529437, 0.117647059, 0.0274509806, 0 }
                        }
                    }
                }
                pass: i16 = 795
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Erosion02.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 25, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Bubble01.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                numFrames: u16 = 6
                startFrame: u16 = 1
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.699999988
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    3.5
                }
                emitterName: string = "sparks"
                importance: u8 = 2
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -400, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -400, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    0x23a0d95c: vec3 = { 20, 10, 20 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, -3 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.76000613 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.196078435, 0.0627451017, 0, 0 }
                            { 0.0980392173, 0.0313725509, 0, 0.181805387 }
                            { 0.0980392173, 0.0313725509, 0, 0.76000613 }
                            { 0.0941176489, 0.0313725509, 0, 0 }
                        }
                    }
                }
                pass: i16 = 2
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.300000012
                                1
                            }
                            values: list[f32] = {
                                0.100000001
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Erosion02.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { -60, 0, 0 }
                            { 60, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.5, 3, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Z_Smoke_SharpShape03.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            1
                        }
                        values: list[f32] = {
                            30
                            15
                            22.5
                            15
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    3.5
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAttractionDefinitions: list[embed] = {
                        VfxFieldAttractionDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 2000
                            }
                            acceleration: embed = ValueFloat {
                                constantValue: f32 = 1000
                            }
                        }
                    }
                }
                emitterName: string = "GlowRadial"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 20, 20 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 3, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    flags: u8 = 1
                    radius: f32 = 20
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.196078435, 0.0627451017, 0, 0 }
                            { 0.0980392173, 0.0313725509, 0, 0.239215687 }
                            { 0.0980392173, 0.0313725509, 0, 1 }
                            { 0.0941176489, 0.0313725509, 0, 0 }
                        }
                    }
                }
                pass: i16 = -50
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.300000012
                                1
                            }
                            values: list[f32] = {
                                0.100000001
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Erosion02.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 180, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 60, 180, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 1, 1, 1 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Z_Smoke_SharpShape03.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    3.5
                }
                emitterName: string = "XY_Icon"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 20, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.113725491, 0.0156862754, 0, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.5
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.190005347, 0.190005347, 0.289997697, 0 }
                            { 0.596078455, 0.596078455, 0.890196085, 0.501960814 }
                            { 0.313725501, 0.541176498, 1, 1 }
                            { 1, 1, 1, 0.500007629 }
                            { 0.192156866, 0.192156866, 0.286274523, 0 }
                        }
                    }
                }
                pass: i16 = -1
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 10
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.300000012
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0.200000003
                                0.5
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_R_WallTexture_01.dds"
                }
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 30, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_R_Yasuo_Skin19_R_dash_sub.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_SoftEnergy_Ver.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.5 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                lifetime: option[f32] = {
                    3.5
                }
                emitterName: string = "spiral_light"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_Vlad_BloodKing_Torus.sco"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.988235295, 0.988235295, 0.988235295, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.988235295, 0.988235295, 0.988235295, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1000
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -360
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 10, 30 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 10, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.400000006, 0.400000006, 0.25 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.400000006, 0.400000006, 0.25 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.800000012, 0.800000012, 0.800000012 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.640000045, 0.200000003, 0.640000045 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1.20000005, 2.56000018, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_E_Slash03.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 3.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh2"
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0xde5b1cd9: flag = true
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Shuriken_Ink.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.596078455, 0.192156866, 0.388235301, 0.592156887 }
                }
                pass: i16 = 1000
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 4, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 1.20000005, 0 }
                            { 0, 24, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.29999995, 5, 5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Noise_Material.dds"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 5, 1 }
                }
            }
        }
        particleName: string = "Volibear_Skin21_Emote_Taunt_01_Child"
        particlePath: string = "Characters/Volibear/Skins/Skin21/Particles/Volibear_Skin21_Emote_Taunt_01_Child"
        flags: u16 = 197
    }
    0x0f3570d2 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.25
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "flash"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 300 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 100, -300 }
                }
                0x563d4a22: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.447058827, 0.192156866, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0136363637
                            0.521029949
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.447058827, 0.192156866, 1 }
                            { 1, 0.447058827, 0.192156866, 0.278431386 }
                            { 1, 0.447058827, 0.192156866, 0 }
                        }
                    }
                }
                pass: i16 = 100
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 200, 200 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.00382409175
                            0.490439773
                            0.996175885
                        }
                        values: list[vec3] = {
                            { 0.529850721, 0.529850721, 0.529850721 }
                            { 0.582089543, 0.582089543, 0.582089543 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Aura_Self.DDS"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.25
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                particleLinger: option[f32] = {
                    10
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "flash_dark"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 300 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 150, -300 }
                }
                0x563d4a22: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_alpha_02.dds"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.862745106, 0.58431375, 0.447058827, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0136363637
                            0.521029949
                            1
                        }
                        values: list[vec4] = {
                            { 0.862745106, 0.58431375, 0.447058827, 1 }
                            { 0.862745106, 0.423913896, 0.173564017, 0.278431386 }
                            { 0.862745106, 0.327674001, 0.212133795, 0 }
                        }
                    }
                }
                pass: i16 = 97
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 200 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.00382409175
                            0.490439773
                            0.996175885
                        }
                        values: list[vec3] = {
                            { 0.529850721, 0.529850721, 0.529850721 }
                            { 0.582089543, 0.582089543, 0.582089543 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Aura_Self.DDS"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "bearHeadBlend3"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 200 }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x31d46b76: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, 2000 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, -50 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Mesh_Anim_RG.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Mesh_Anim_RG.skl"
                        mAnimationName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Mesh_Anim_RG.anm"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.549019635, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0743801668
                            0.690374553
                            0.792537332
                            0.901492536
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.549019635, 0, 0 }
                            { 1, 0.549019635, 0, 1 }
                            { 1, 0.549019635, 0, 1 }
                            { 1, 0.549019635, 0, 0.867318451 }
                            { 1, 0.549019635, 0, 0.23031646 }
                            { 1, 0.549019635, 0, 0 }
                        }
                    }
                }
                pass: i16 = 99
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.388585657
                                0.551546514
                                0.711342216
                                1
                            }
                            values: list[f32] = {
                                1
                                0.181818187
                                0.0181818176
                                0.5
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_W_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 0 }
                    fresnel: f32 = 0.00100000005
                    fresnelColor: vec4 = { 0.890196085, 0.745098054, 0.490196079, 1 }
                }
                depthBiasFactors: vec2 = { 1, -80 }
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.850000024, 0.850000024, 0.850000024 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0674931109
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin21/Volibear_Skin21_TX_CM.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Base_Indicator_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 1, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "bearHeadBlend4"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 200 }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x31d46b76: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, 2000 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, -50 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Mesh_Anim_RG.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Mesh_Anim_RG.skl"
                        mAnimationName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Mesh_Anim_RG.anm"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.113725491, 0.113725491, 0.113725491, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0743801668
                            0.690374553
                            0.792537332
                            0.901492536
                            1
                        }
                        values: list[vec4] = {
                            { 0.113725491, 0.113725491, 0.113725491, 0 }
                            { 0.113725491, 0.113725491, 0.113725491, 1 }
                            { 0.113725491, 0.113725491, 0.113725491, 1 }
                            { 0.113725491, 0.113725491, 0.113725491, 0.867318451 }
                            { 0.113725491, 0.113725491, 0.113725491, 0.23031646 }
                            { 0.113725491, 0.113725491, 0.113725491, 0 }
                        }
                    }
                }
                pass: i16 = 98
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.699999988
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_W_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { 1, -80 }
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.850000024, 0.850000024, 0.850000024 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0674931109
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin21/Volibear_Skin21_TX_CM.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_E_Trail03.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 2 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
                    }
                }
            }
        }
        particleName: string = "Volibear_Skin21_W_Chomp"
        particlePath: string = "Characters/Volibear/Skins/Skin21/Particles/Volibear_Skin21_W_Chomp"
        flags: u16 = 198
    }
    0x3085af3d = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "backBlend1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.200000003, 0, 1 }
                }
                pass: i16 = -6
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 45, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh"
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0xde5b1cd9: flag = true
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Shuriken.scb"
                    }
                }
                blendMode: u8 = 1
                alphaRef: u8 = 0
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 90 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -180, 0, 0 }
                }
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 5, 5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin21/Volibear_Skin21_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "backBlend2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.749019623, 0, 1 }
                }
                pass: i16 = -2
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 45, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                particleLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "Basic"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 50, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    flags: u8 = 1
                    0x23a0d95c: vec3 = { 0, 0, 20 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.107189544, 0, 0.0248366017, 0 }
                            { 0.107189544, 0, 0.0483660139, 0.568627477 }
                            { 0.071895428, 0, 0.0248366017, 1 }
                            { 0.0836601332, 0, 0.0326797403, 0 }
                        }
                    }
                }
                pass: i16 = -3
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.200000003
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Z_Splats_02_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 25, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 25, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_BasicAttack_Splats_02.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                numFrames: u16 = 6
                startFrame: u16 = 1
                texDiv: vec2 = { 4, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                emitterName: string = "Ink"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 4, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    flags: u8 = 1
                    0x23a0d95c: vec3 = { 0, 0, 20 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.113725491, 0.00392156886, 0.0509803928, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.662745118, 1, 0.152941182, 0 }
                            { 0.65882355, 1, 0.20784314, 1 }
                            { 0.0784313753, 0.117647059, 0.0313725509, 1 }
                            { 0.0823529437, 0.117647059, 0.0274509806, 0 }
                        }
                    }
                }
                pass: i16 = -4
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Erosion02.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 25, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Bubble01.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                numFrames: u16 = 6
                startFrame: u16 = 1
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "XY_Icon"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 20, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.113725491, 0.00392156886, 0.0588235296, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.5
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.190005347, 0.190005347, 0.289997697, 0 }
                            { 0.596078455, 0.596078455, 0.890196085, 0.501960814 }
                            { 0.313725501, 0.541176498, 1, 1 }
                            { 1, 1, 1, 0.500007629 }
                            { 0.192156866, 0.192156866, 0.286274523, 0 }
                        }
                    }
                }
                pass: i16 = -5
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 10
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.300000012
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0.200000003
                                0.5
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_R_WallTexture_01.dds"
                }
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 30, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_R_Yasuo_Skin19_R_dash_sub.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_SoftEnergy_Ver.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.5 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh2"
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0xde5b1cd9: flag = true
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Shuriken_Ink.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.596078455, 0.192156866, 0.388235301, 0.592156887 }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 90 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -180, 0, 0 }
                }
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 5, 5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Noise_Material.dds"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 5, 1 }
                }
            }
        }
        particleName: string = "Volibear_Skin21_Idle_Shuriken"
        particlePath: string = "Characters/Volibear/Skins/Skin21/Particles/Volibear_Skin21_Idle_Shuriken"
        flags: u16 = 197
    }
    0x361d29bc = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin21_Idle_Breath"
        particlePath: string = "Characters/Volibear/Skins/Skin21/Particles/Volibear_Skin21_Idle_Breath"
    }
    0x7172949d = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh"
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0xde5b1cd9: flag = true
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Shuriken.scb"
                    }
                }
                blendMode: u8 = 1
                alphaRef: u8 = 0
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -180, 0, 0 }
                }
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 5, 5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin21/Volibear_Skin21_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "backBlend3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.200000003, 0, 1 }
                }
                pass: i16 = -6
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 45, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "backBlend4"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.749019623, 0, 1 }
                }
                pass: i16 = -1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 45, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                particleLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "Basic"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 50, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    flags: u8 = 1
                    0x23a0d95c: vec3 = { 0, 0, 20 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.107189544, 0, 0.0248366017, 0 }
                            { 0.107189544, 0, 0.0483660139, 0.568627477 }
                            { 0.071895428, 0, 0.0248366017, 1 }
                            { 0.0836601332, 0, 0.0326797403, 0 }
                        }
                    }
                }
                pass: i16 = -2
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.200000003
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Z_Splats_02_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 25, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 25, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_BasicAttack_Splats_02.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                numFrames: u16 = 6
                startFrame: u16 = 1
                texDiv: vec2 = { 4, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                emitterName: string = "Ink"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 4, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    flags: u8 = 1
                    0x23a0d95c: vec3 = { 0, 0, 20 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.113725491, 0.00392156886, 0.0509803928, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.662745118, 1, 0.152941182, 0 }
                            { 0.65882355, 1, 0.20784314, 1 }
                            { 0.0784313753, 0.117647059, 0.0313725509, 1 }
                            { 0.0823529437, 0.117647059, 0.0274509806, 0 }
                        }
                    }
                }
                pass: i16 = -3
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Erosion02.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 25, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Bubble01.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                numFrames: u16 = 6
                startFrame: u16 = 1
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "XY_Icon"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 5, -20, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.113725491, 0.00392156886, 0.0588235296, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.5
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.190005347, 0.190005347, 0.289997697, 0 }
                            { 0.596078455, 0.596078455, 0.890196085, 0.501960814 }
                            { 0.313725501, 0.541176498, 1, 1 }
                            { 1, 1, 1, 0.500007629 }
                            { 0.192156866, 0.192156866, 0.286274523, 0 }
                        }
                    }
                }
                pass: i16 = -4
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 10
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.300000012
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0.200000003
                                0.5
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_R_WallTexture_01.dds"
                }
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, -90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 30, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_R_Yasuo_Skin19_R_dash_sub.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_SoftEnergy_Ver.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.5 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh2"
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0xde5b1cd9: flag = true
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Shuriken_Ink.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.596078455, 0.192156866, 0.388235301, 0.592156887 }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -180, 0, 0 }
                }
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 5, 5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Noise_Material.dds"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 5, 1 }
                }
            }
        }
        particleName: string = "Volibear_Skin21_Idle_Shuriken2"
        particlePath: string = "Characters/Volibear/Skins/Skin21/Particles/Volibear_Skin21_Idle_Shuriken2"
        flags: u16 = 197
    }
    0x9aedf4cc = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.800000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLinger: option[f32] = {
                    0.449999988
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "Hand_Ink"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xe90a842c
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            0xe90a842c
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 0.772549033 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.024813896
                            0.924242377
                            0.955334961
                            0.981518269
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.964705884 }
                            { 0.482352942, 0.482352942, 0.482352942, 0.850980401 }
                            { 0.180392161, 0.180392161, 0.180392161, 0 }
                        }
                    }
                }
                pass: i16 = -13
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -6 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Noise_Material.dds"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 5, 1 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.800000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLinger: option[f32] = {
                    0.449999988
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "Hand_Ink1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xa0e98faf
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            0xa0e98faf
                            0x811c9dc5
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.024813896
                            0.924242377
                            0.955334961
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.964705884 }
                            { 1, 1, 1, 0.850980401 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -14
                alphaRef: u8 = 0
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.0500000007
                    fresnelColor: vec4 = { 1, 0.282352954, 0, 0 }
                }
                depthBiasFactors: vec2 = { -1, 0 }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin21/Particles/Volibear_Skin21_Tex_CM_Red.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    12
                }
                emitterName: string = "Ground"
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    flags: u8 = 1
                    radius: f32 = 25
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.23137255, 0.105882354, 0.0705882385, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -996
                alphaRef: u8 = 80
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.300000012
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_E_AlphaSlice_1.dds"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 360, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 65, 90, 90 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Ink_05.dds"
                birthFrameRate: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                lifetime: option[f32] = {
                    12
                }
                emitterName: string = "Ground_Glow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 20 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    flags: u8 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.286274523, 0.203921571, 0.184313729, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.159268931
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.286274523, 0.203921571, 0.184313729, 0 }
                            { 0.286274523, 0.203921571, 0.184313729, 1 }
                            { 0.286274523, 0.203921571, 0.184313729, 1 }
                            { 0.286274523, 0.203921571, 0.184313729, 0 }
                        }
                    }
                }
                pass: i16 = -5
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 180, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 180, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 100, 100 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Q_Glow.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.800000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLinger: option[f32] = {
                    0.150000006
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "bodyAlpha"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                            0xd5977cbe
                            0x8ecfcde6
                            0xbbd77415
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            0x8edf6853
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.024813896
                            0.924242377
                            0.955334961
                            0.981518269
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.482352942, 0.482352942, 0.482352942, 0.964705884 }
                            { 0.319996953, 0.319996953, 0.319996953, 0.62999922 }
                            { 0.164705887, 0.164705887, 0.164705887, 0 }
                        }
                    }
                }
                pass: i16 = -20
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin21/Particles/Volibear_Skin21_Tex_CM_Red.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 11.4499998
                }
                particleLinger: option[f32] = {
                    0.150000006
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "bodyFresnel"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                            0x8ecfcde6
                            0xbbd77415
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.024813896
                            0.924242377
                            0.955334961
                            0.981518269
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 0.964705884 }
                            { 0, 0, 0, 0.850980401 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = -19
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = -1.10000002
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_alpha_Ero.dds"
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 0 }
                    fresnel: f32 = 0.0599999987
                    fresnelColor: vec4 = { 1, 0.282352954, 0, 1 }
                }
                depthBiasFactors: vec2 = { -1, -3 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin21/Particles/Volibear_Skin21_Tex_CM_Red.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    0.150000006
                }
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "Star"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.649999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.419607848, 0.247058824, 0.129411772, 1 }
                            { 1, 0.368627459, 0.0784313753, 1 }
                            { 0.196078435, 0.137254909, 0.109803922, 1 }
                            { 0.0862745121, 0.0862745121, 0.109803922, 0 }
                        }
                    }
                }
                pass: i16 = 5
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_skin5_R_color-hold.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Base_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.400000006, 0.200000003 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.649999976
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "AV_ChromaticAbberation_B1"
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 0, -1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, -1 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 5
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.200000003 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.435294122, 0.203921571, 0.156862751, 0 }
                            { 0.176470593, 0.101960786, 0.0588235296, 1 }
                            { 0.113725491, 0.0156862754, 0, 0 }
                        }
                    }
                }
                pass: i16 = -17
                meshRenderFlags: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.08000004, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.99000001
                                    1.00999999
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1.08000004, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/3161color-hold.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Noise_Material.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "OuterSplash"
                0x563d4a22: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_splash_ring.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.215686277, 0.13333334, 0.0862745121, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.00999999978
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0.215686277, 0.13333334, 0.0862745121, 1 }
                            { 0.215686277, 0.13333334, 0.0862745121, 0.568627477 }
                            { 0.215686277, 0.13333334, 0.0862745121, 0 }
                        }
                    }
                }
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 60
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Wall_Erosion.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 90, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2.5, 0.5, 2.55999994 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0910929963
                            0.192372322
                            0.28441301
                            0.42206499
                            0.551597953
                            0.668016016
                            0.779374063
                            0.871413767
                            0.899999976
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2.29999995, 2.53206515, 2.29999995 }
                            { 2.875, 3.7750001, 2.875 }
                            { 3.2249999, 4.17500019, 3.2249999 }
                            { 3.55285978, 4.25, 3.54999995 }
                            { 3.75, 3.6605978, 3.75 }
                            { 3.875, 2.94266295, 3.875 }
                            { 4, 2.0711956, 4 }
                            { 4.125, 1.14619565, 4.125 }
                            { 4.2750001, -0, 4.2750001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Z_splash_ring.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.200000003 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 12
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    0.150000006
                }
                lifetime: option[f32] = {
                    12.5
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "EndFlash4"
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x5e4d31b7: flag = true
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {}
                        ValueFloat {}
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 0, 0 }
                        { 0, 0, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                            0xd5977cbe
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 0.972549021 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0480526648
                            0.187859938
                            0.410504252
                            0.984782636
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.566265047 }
                            { 1, 1, 1, 0.258187443 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -15
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_skin5_R_color-hold.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.649999976
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.800000012
                        }
                    }
                }
                lifetime: option[f32] = {
                    12
                }
                emitterName: string = "EdgeGlow"
                importance: u8 = 2
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 1, -1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, -1 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    flags: u8 = 1
                    radius: f32 = 5
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                        }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.772549033 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.196078435, 0.145098045, 0.137254909, 0 }
                            { 0.149019614, 0.113725491, 0.101960786, 1 }
                            { 0.0862745121, 0.0862745121, 0.109803922, 0.458823532 }
                            { 0.0862745121, 0.0862745121, 0.109803922, 0 }
                        }
                    }
                }
                pass: i16 = -100
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 1.39999998
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.560000002
                                1.39999998
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_VGU_Generic_Erosion01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1.05999994, 1.05999994 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.10000002, 1, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/3161color-hold.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1.5, 1 }
                }
                textureMult: pointer = 0xb097c1bd {}
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                lifetime: option[f32] = {
                    12
                }
                emitterName: string = "Praxis"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.25
                        }
                        values: list[f32] = {
                            1
                            0
                        }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_sru_clouds.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.113725491, 0.0156862754, 0, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.349999994
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.125490203, 0.0705882385, 0.117647059, 0.376470596 }
                            { 0.0823529437, 0.0941176489, 0.125490203, 0 }
                        }
                    }
                }
                pass: i16 = 50
                disableBackfaceCull: bool = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.70000005, 1, 1.70000005 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0700000003
                            0.158213556
                            0.322381943
                            0.519762874
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                            { 0.571055293, 0.575999975, 0.57209301 }
                            { 0.767441869, 2, 0.767441869 }
                            { 0.869767427, 4, 0.876150846 }
                            { 0.91749537, 4, 0.912844181 }
                            { 1, 5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_VGU_Awaken_Ribbonmask01.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { -0.25, 0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { -0.25, 0.5 }
                            { -0, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLinger: option[f32] = {
                    0.449999988
                }
                isSingleParticle: flag = true
                emitterName: string = "Spike2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xbbd77415
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            0xbbd77415
                            0x811c9dc5
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.501960814, 0, 0.34117648 }
                }
                pass: i16 = -18
                alphaRef: u8 = 0
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.200000003
                    fresnelColor: vec4 = { 1, 0.501960814, 0, 0 }
                }
                depthBiasFactors: vec2 = { -1, -6 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin21/Volibear_Skin21_TX_CM.dds"
                materialOverrideDefinitions: list[embed] = {
                    VfxMaterialOverrideDefinitionData {}
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLinger: option[f32] = {
                    0.449999988
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "Spike_Ink1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xbbd77415
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            0xbbd77415
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.176470593, 0.101960786, 0.0588235296, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.00999999978
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.86999315 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 36
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -6 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Noise05.dds"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 1 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 10, 5 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLinger: option[f32] = {
                    0.449999988
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "Spike_Ink2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xbbd77415
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            0xbbd77415
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.384313732, 0.137254909, 0.0392156877, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.00999999978
                            0.949999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.86999315 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -17
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -6 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Noise05.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 0.5 }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 1 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 10, 5 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    12
                }
                emitterName: string = "Shoulder"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 300, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.282352954, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.282352954, 0, 0 }
                            { 1, 0.282352954, 0, 1 }
                            { 1, 0.282352954, 0, 0 }
                        }
                    }
                }
                pass: i16 = -1
                depthBiasFactors: vec2 = { 1, 50 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 140, 70 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Q_Glow.dds"
            }
        }
        particleName: string = "Volibear_Skin21_R_Buf_Max"
        particlePath: string = "Characters/Volibear/Skins/Skin21/Particles/Volibear_Skin21_R_Buf_Max"
    }
    0xa0167183 = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin21_Idle_pawSpark"
        particlePath: string = "Characters/Volibear/Skins/Skin21/Particles/Volibear_Skin21_Idle_pawSpark"
        flags: u16 = 204
    }
    0xb2e2a50f = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh"
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0xde5b1cd9: flag = true
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Shuriken.scb"
                    }
                }
                blendMode: u8 = 1
                pass: i16 = 900
                alphaRef: u8 = 0
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.29999995, 5, 5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin21/Volibear_Skin21_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "backBlend1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.219607845, 0.0235294122, 1 }
                }
                pass: i16 = 800
                alphaRef: u8 = 0
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 45, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                emitterName: string = "Basic"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 50, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    flags: u8 = 1
                    0x23a0d95c: vec3 = { 0, 0, 20 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0.113725491, 0.0156862754, 0, 0 }
                            { 0.113725491, 0.0156862754, 0, 0.568627477 }
                            { 0.0784313753, 0.00784313772, 0, 1 }
                            { 0.0901960805, 0.0117647061, 0, 0 }
                        }
                    }
                }
                pass: i16 = 796
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.200000003
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Z_Splats_02_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 25, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 25, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_BasicAttack_Splats_02.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                numFrames: u16 = 6
                startFrame: u16 = 1
                texDiv: vec2 = { 4, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "Ink"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 30, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 4, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 150, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    flags: u8 = 1
                    0x23a0d95c: vec3 = { 0, 0, 20 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.113725491, 0.0156862754, 0, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.662745118, 1, 0.152941182, 0 }
                            { 0.65882355, 1, 0.20784314, 1 }
                            { 0.0784313753, 0.117647059, 0.0313725509, 1 }
                            { 0.0823529437, 0.117647059, 0.0274509806, 0 }
                        }
                    }
                }
                pass: i16 = 795
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Erosion02.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 25, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Bubble01.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                numFrames: u16 = 6
                startFrame: u16 = 1
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                emitterName: string = "XY_Icon"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 20, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.113725491, 0.0156862754, 0, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.5
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.190005347, 0.190005347, 0.289997697, 0 }
                            { 0.596078455, 0.596078455, 0.890196085, 0.501960814 }
                            { 0.313725501, 0.541176498, 1, 1 }
                            { 1, 1, 1, 0.500007629 }
                            { 0.192156866, 0.192156866, 0.286274523, 0 }
                        }
                    }
                }
                pass: i16 = -1
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 10
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.300000012
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0.200000003
                                0.5
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_R_WallTexture_01.dds"
                }
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 30, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_R_Yasuo_Skin19_R_dash_sub.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_SoftEnergy_Ver.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.5 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "XY_Ringlight"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 0.384313732, 0.137254909, 0.0392156877, 0.501960814 }
                            { 1, 0.31764707, 0, 1 }
                            { 0.384313732, 0.137254909, 0.0392156877, 0.501960814 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 3
                colorLookUpTypeY: u8 = 3
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 90, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 75, 0.5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.949999988, 0, 0 }
                            { 1, 1, 1 }
                            { 1.5, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Idle_Ringlight.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "backBlend2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -5, 0, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.519996941, 0.130006865, 0.800000012 }
                }
                pass: i16 = 797
                alphaRef: u8 = 0
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 45, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "backBlend3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.76000613, 0.0500038154, 1 }
                }
                pass: i16 = 798
                alphaRef: u8 = 0
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 45, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_Aura_Self.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.699999988
                        }
                    }
                }
                lifetime: option[f32] = {
                    10
                }
                emitterName: string = "sparks"
                importance: u8 = 2
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -400, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -400, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    0x23a0d95c: vec3 = { 20, 10, 20 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 5, -3 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.76000613 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.196078435, 0.0627451017, 0, 0 }
                            { 0.0980392173, 0.0313725509, 0, 0.181805387 }
                            { 0.0980392173, 0.0313725509, 0, 0.76000613 }
                            { 0.0941176489, 0.0313725509, 0, 0 }
                        }
                    }
                }
                pass: i16 = 2
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.300000012
                                1
                            }
                            values: list[f32] = {
                                0.100000001
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Erosion02.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { -60, 0, 0 }
                            { 60, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0.5, 3, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Z_Smoke_SharpShape03.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.20000005
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            1
                        }
                        values: list[f32] = {
                            30
                            15
                            22.5
                            15
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    10
                }
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAttractionDefinitions: list[embed] = {
                        VfxFieldAttractionDefinitionData {
                            radius: embed = ValueFloat {
                                constantValue: f32 = 2000
                            }
                            acceleration: embed = ValueFloat {
                                constantValue: f32 = 1000
                            }
                        }
                    }
                }
                emitterName: string = "GlowRadial"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 20 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 20, 20 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 3, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    flags: u8 = 1
                    radius: f32 = 20
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.196078435, 0.0627451017, 0, 0 }
                            { 0.0980392173, 0.0313725509, 0, 0.239215687 }
                            { 0.0980392173, 0.0313725509, 0, 1 }
                            { 0.0941176489, 0.0313725509, 0, 0 }
                        }
                    }
                }
                pass: i16 = -50
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.300000012
                                1
                            }
                            values: list[f32] = {
                                0.100000001
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Erosion02.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 180, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 180, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 1, 1, 1 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Z_Smoke_SharpShape03.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh2"
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0xde5b1cd9: flag = true
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Shuriken_Ink.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.596078455, 0.192156866, 0.388235301, 0.592156887 }
                }
                pass: i16 = 1000
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.29999995, 5, 5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Noise_Material.dds"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 5, 1 }
                }
            }
        }
        particleName: string = "Volibear_Skin21_Z_Shuriken"
        particlePath: string = "Characters/Volibear/Skins/Skin21/Particles/Volibear_Skin21_Z_Shuriken"
        flags: u16 = 197
    }
    0xe38720b5 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                lifetime: option[f32] = {
                    0.699999988
                }
                emitterName: string = "Avatar_Body_Burst"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0x8ee07624
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            0x8ee07624
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/VS_Color_Rampdown.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.560006082, 0.0200045779, 0.900007606 }
                            { 1, 0.470588237, 0.0392156877, 0.729411781 }
                            { 0.87843138, 0.290196091, 0, 0.450980395 }
                            { 0.666666687, 0, 0, 0.270588249 }
                        }
                    }
                }
                pass: i16 = 20
                meshRenderFlags: u8 = 0
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 1, 0.333333343, 0, 1 }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.10000002, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin21/Volibear_Skin21_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                lifetime: option[f32] = {
                    0.600000024
                }
                isSingleParticle: flag = true
                emitterName: string = "DistortFlash"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 250, 0 }
                }
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Z_Cas_Distort.dds"
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.510002315 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 98
                distortionDefinition: pointer = VfxDistortionDefinitionData {
                    distortion: f32 = 0.0500000007
                    normalMapTexture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/distort.dds"
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 0 }
                }
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 220, 270, 270 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.200000003, 0.200000003 }
                            { 1, 1, 1 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_skin5_R_color-hold.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "GlowBottom"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 250, 0 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.219607845, 0.0235294122, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.219607845, 0.0235294122, 1 }
                            { 1, 0.219607845, 0.0235294122, 0 }
                        }
                    }
                }
                pass: i16 = -15
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 10, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_fuzzyshadow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.29999995
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                lifetime: option[f32] = {
                    2.20000005
                }
                isSingleParticle: flag = true
                emitterName: string = "mesh_ground"
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 50, 0 }
                        }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 250, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin20_Z_weaponswipe6.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.770000756 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.152941182, 0.0196078438, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.144544408, 0.0185313337, 0, 1 }
                            { 0.112756632, 0.0144559788, 0, 1 }
                            { 0.152941182, 0.018992696, 0, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.200000003
                                1
                            }
                            values: list[f32] = {
                                0.0599999987
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin20_Z_Wisps.dds"
                }
                depthBiasFactors: vec2 = { -1, -100 }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.400000006, 1.25999999, 1.25999999 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0.400000006, 1.25999999, 1.25999999 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0.899999976, 0.899999976 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                            { 1.29999995, 1, 1.29999995 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Q_CloudTxt.dds"
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 0.400000006, 0 }
                            { 0.100000001, 0 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Q_CloudTxt.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "SnowFlash"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 250, 0 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.764705896, 0.0549019612, 0.239215687 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.814814806
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 9999
                colorLookUpTypeY: u8 = 3
                depthBiasFactors: vec2 = { -1, -100 }
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.118518516
                            0.383333355
                            0.634722233
                            0.995370388
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.02535212, 1.02535212, 1.02535212 }
                            { 1.61408448, 1.61408448, 1.61408448 }
                            { 1.86197186, 1.86197186, 1.86197186 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_KogMaw_Skin05_Z_tar_Flash.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.400000006
                        }
                    }
                }
                lifetime: option[f32] = {
                    10
                }
                isSingleParticle: flag = true
                emitterName: string = "Swirls"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 250, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Aatrox_Base_Z_swirl.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.490196079, 0.129411772, 0, 0.729411781 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.0980392173 }
                            { 0.137254909, 0.113725491, 0.101960786, 0 }
                        }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.100000001
                    fresnelColor: vec4 = { 0, 0, 0, 1 }
                }
                disableBackfaceCull: bool = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 7, 7, 7 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 7, 7, 7 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.699999988, 0.699999988, 0.699999988 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Ele_Glow.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 2 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.100000001 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                texDiv: vec2 = { 0.5, 1 }
                uvScale: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 1, 3 }
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Hit01.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.5, 3 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            100
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                emitterName: string = "Ground_Flames"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 150, 150 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    radius: f32 = 50
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 300, 50 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.137254909, 0.113725491, 0.101960786, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.00999999978
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.764705896, 0.0549019612, 1 }
                            { 1, 0.666666687, 0, 1 }
                            { 1, 0.282352954, 0, 0.490196079 }
                            { 0.301960796, 0.0352941193, 0, 0 }
                        }
                    }
                }
                pass: i16 = 150
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_E_LinearSplashes_02_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 80, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 80, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 0.150000006, 0.300000012, 0.5 }
                            { 1.5, 1, 1 }
                            { 1.70000005, 1.5, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Z_Goop_02_Rendered.dds"
                birthFrameRate: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    4
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            100
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.5
                        }
                    }
                }
                emitterName: string = "Ground_Flames1"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 200, 100 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x3dbe415d {
                    radius: f32 = 50
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 350, 50 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.137254909, 0.113725491, 0.101960786, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.00999999978
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.764705896, 0.0549019612, 1 }
                            { 1, 0.666666687, 0, 1 }
                            { 1, 0.282352954, 0, 0.490196079 }
                            { 0.301960796, 0.0352941193, 0, 0 }
                        }
                    }
                }
                pass: i16 = 150
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_E_LinearSplashes_02_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 80, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 80, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 0.150000006, 0.300000012, 0.5 }
                            { 1.5, 1, 1 }
                            { 1.70000005, 1.5, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Z_Goop_02_Rendered.dds"
                birthFrameRate: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    4
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1
                        }
                    }
                }
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.649999976
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            1.5
                        }
                    }
                }
                emitterName: string = "swirl_mesh_dark"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.200000003, 0 }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -30, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -30, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 220, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Z_Despairpool_tar_swirl_01.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.900007606 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.333333343, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.333333343, 0, 0 }
                            { 1, 0.333333343, 0, 1 }
                            { 1, 0.333333343, 0, 1 }
                            { 1, 0.333333343, 0, 0 }
                        }
                    }
                }
                pass: i16 = 1
                colorLookUpTypeX: u8 = 3
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 50
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.300000012
                                0.699999988
                            }
                            values: list[f32] = {
                                1
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.25
                    erosionFeatherOut: f32 = 0.25
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_E_Swipe_Mult_01.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                0x2cf8568e: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 45, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -45, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_R_Trail04.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 0.800000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.100000001, 0.800000012 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 1.5, 1 }
                            { 0.5, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Wind_splash_01.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.800000012
                        }
                    }
                }
                emitterName: string = "Swirls1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                        }
                        values: list[f32] = {
                            1
                            0
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 250, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Aatrox_Base_Z_swirl.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.490196079, 0.129411772, 0, 0.729411781 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.0980392173 }
                            { 0.168627456, 0.141176477, 0.125490203, 0 }
                        }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.100000001
                    fresnelColor: vec4 = { 0, 0, 0, 1 }
                }
                disableBackfaceCull: bool = true
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 7, 7, 7 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.29999995
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 7, 7, 7 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Ele_Glow.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 2 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.100000001 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                texDiv: vec2 = { 0.5, 1 }
                uvScale: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { 1, 3 }
                            { 1, 1 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Hit01.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.5, 3 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                emitterName: string = "Temp_Avatar"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xe90a842c
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            0xe90a842c
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/color-rampdown.Leblanc_Rework.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.280003041, 0, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 600
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { 0, -50 }
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_R_WallTexture_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1.5, 1.5 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.39999998
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                lifetime: option[f32] = {
                    3
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Avatar1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/color-rampdown.Leblanc_Rework.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 0.400000006 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 501
                alphaRef: u8 = 0
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.0500000007
                    fresnelColor: vec4 = { 1, 0.321568638, 0.0549019612, 0 }
                }
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/3161color-hold.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1.5, 1.5 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                lifetime: option[f32] = {
                    0.600000024
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh1"
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Zilean_Skin14_helix_01.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.152941182, 0.0196078438, 0, 0.600000024 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.00191570877
                            0.0461685844
                            0.496168584
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.200300142 }
                        }
                    }
                }
                pass: i16 = 50
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.600000024
                                1
                            }
                            values: list[f32] = {
                                0
                                0.100000001
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_ErosionPack01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 5, 10 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 1, 1 }
                            { 1, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Morg_Skin35_MeshMult.dds"
                uvMode: u8 = 2
                texAddressModeBase: u8 = 2
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_BeamTrail01.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 3 }
                    }
                    uvScrollClampMult: flag = true
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, 3 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[vec2] = {
                                { 0, 3 }
                                { 0, 0.600000024 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                lifetime: option[f32] = {
                    8
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Avatar2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/color-rampdown.Leblanc_Rework.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 500
                alphaRef: u8 = 0
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.0299999993
                    fresnelColor: vec4 = { 1, 0.321568638, 0.0549019612, 0 }
                }
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/3161color-hold.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1.5, 1.5 }
                }
            }
        }
        particleName: string = "Volibear_Skin21_Z_End_01"
        particlePath: string = "Characters/Volibear/Skins/Skin21/Particles/Volibear_Skin21_Z_End_01"
        flags: u16 = 197
    }
    0xefd2b44c = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 99
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "Avatar"
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x5e4d31b7: flag = true
                    0xb2dcc7dc: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0.00816326495
                                1
                            }
                            values: list[vec3] = {
                                { 1, 0, 0 }
                                { 0.5, 0, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            "BODY"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                }
                pass: i16 = 20
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionFeatherIn: f32 = 0.5
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Passive_Glow_A.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 0 }
                    fresnel: f32 = 0.100000001
                    fresnelColor: vec4 = { 1, 0.282352954, 0, 1 }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin21/Volibear_Skin21_TX_CM.dds"
                textureMult: pointer = 0xb097c1bd {
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.400000006, 0.400000006 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        -1
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.400000006, 0.400000006 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                lifetime: option[f32] = {
                    12
                }
                emitterName: string = "Ground_Glow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 20 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    flags: u8 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -150, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.286274523, 0.203921571, 0.184313729, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.159268931
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.286274523, 0.203921571, 0.184313729, 0 }
                            { 0.286274523, 0.203921571, 0.184313729, 1 }
                            { 0.286274523, 0.203921571, 0.184313729, 1 }
                            { 0.286274523, 0.203921571, 0.184313729, 0 }
                        }
                    }
                }
                pass: i16 = -5
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 180, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 90, 180, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 100, 100 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Q_Glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    0.449999988
                }
                isSingleParticle: flag = true
                emitterName: string = "Spike1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xbbd77415
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            0xbbd77415
                            0x811c9dc5
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                }
                pass: i16 = 33
                alphaRef: u8 = 0
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    fresnel: f32 = 0.5
                    fresnelColor: vec4 = { 1, 0.219607845, 0.0235294122, 0 }
                }
                depthBiasFactors: vec2 = { -1, -6 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Q_White.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                emitterName: string = "Shoulder"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 50, 0 }
                }
                0x563d4a22: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.282352954, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.282352954, 0, 0 }
                            { 1, 0.282352954, 0, 1 }
                            { 1, 0.282352954, 0, 0 }
                        }
                    }
                }
                pass: i16 = 5
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 140, 70 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_Q_Glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                lifetime: option[f32] = {
                    12
                }
                emitterName: string = "Praxis"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.25
                        }
                        values: list[f32] = {
                            1
                            0
                        }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -50, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/common_sru_clouds.scb"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.113725491, 0.0156862754, 0, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.349999994
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.60999465 }
                            { 0.130006865, 0.0699931309, 0.11999695, 0.220004573 }
                            { 0.0823529437, 0.0941176489, 0.125490203, 0 }
                        }
                    }
                }
                pass: i16 = 50
                disableBackfaceCull: bool = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    360
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.70000005, 1, 1.70000005 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0700000003
                            0.158213556
                            0.322381943
                            0.519762874
                            1
                        }
                        values: list[vec3] = {
                            { 0.200000003, 0.5, 0.200000003 }
                            { 0.571055293, 0.800000012, 0.57209301 }
                            { 0.767441869, 2, 0.767441869 }
                            { 0.869767427, 4, 0.876150846 }
                            { 0.91749537, 4, 0.912844181 }
                            { 1, 5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_VGU_Awaken_Ribbonmask01.dds"
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 1, 1 }
                        }
                    }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { -0.25, 0.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec2] = {
                            { -0.25, 0.5 }
                            { -0, 0 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    0.449999988
                }
                isSingleParticle: flag = true
                emitterName: string = "Spike3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xbbd77415
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            0xbbd77415
                            0x811c9dc5
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.280003041, 0, 0.340001523 }
                }
                pass: i16 = 30
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -6 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin21/Volibear_Skin21_TX_CM.dds"
                materialOverrideDefinitions: list[embed] = {
                    VfxMaterialOverrideDefinitionData {}
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 11.4499998
                }
                particleLinger: option[f32] = {
                    0.150000006
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "handFresnel"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                            0x8ecfcde6
                            0xbbd77415
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.024813896
                            0.924242377
                            0.955334961
                            0.981518269
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 0.964705884 }
                            { 0, 0, 0, 0.850980401 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 7
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = -1.10000002
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin19/Particles/Volibear_Skin19_alpha_Hand.dds"
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 0 }
                    fresnel: f32 = 0.100000001
                    fresnelColor: vec4 = { 1, 0.501960814, 0, 1 }
                }
                depthBiasFactors: vec2 = { -1, -3 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin21/Volibear_Skin21_TX_CM.dds"
            }
        }
        particleName: string = "Volibear_Skin21_Passive_maxStacks_Aura_01"
        particlePath: string = "Characters/Volibear/Skins/Skin21/Particles/Volibear_Skin21_Passive_maxStacks_Aura_01"
    }
    0x944fefb0 = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Volibear_R_attack_buf_L" = 0xe14c451d
            "Volibear_R_attack_buf_R" = 0xe34c4843
            0x9302b6d3 = 0x639299b2
            0xbabd2161 = 0x361d29bc
            0xdeb570a5 = 0x9aedf4cc
            0x339465c4 = 0x2aebbb2d
            0x5d587cca = 0xb2e1ef6f
            0x3426454d = 0xefd2b44c
            0x86cad419 = 0x2db407d8
            0x255cc173 = 0xed12ce0c
            0xeeb9b013 = 0x0f3570d2
            0x430a78d7 = 0xb525a488
            0xefccc0de = 0xb525a488
            0x26e4bfc3 = 0x4c677f0c
            0x19a7d548 = 0x23361723
            0x5175695e = 0xba28602d
            0x79ea8ec0 = 0xbe99e573
            0xca178bf5 = 0x54a2837c
            0x2076dd33 = 0xfd7d89f2
            0xcfe5ced8 = 0x30794451
            0x34a4196b = 0x09f51756
            0x7e2af041 = 0xf4349648
            0x4c352fd2 = 0xb70085ff
            0x4b352e3f = 0xb8008792
            0x4a352cac = 0xb9008925
            0xe36387f0 = 0x1b3b8c85
            0xe6638ca9 = 0x183b87cc
            0xe5638b16 = 0x193b895f
            0xcfdc69a6 = 0xc3942691
            0xcedc6813 = 0xc09421d8
            0xcddc6680 = 0xc194236b
            0x01ab2a3c = 0x53a3fae3
            0x04ab2ef5 = 0x54a3fc76
            0x03ab2d62 = 0x55a3fe09
            0x95bf28e2 = 0xf3c3643d
            0x94bf274f = 0xf0c35f84
            0x93bf25bc = 0xf1c36117
            0x2e517920 = 0x296c0567
            0x31517dd9 = 0x2a6c06fa
            0x30517c46 = 0x2b6c088d
            0x178c0831 = 0x3bf74878
            0x04fe08a9 = 0xa31aaa3c
            0x04719679 = 0xf8cc049e
            0x2cd330c5 = 0xfe51762c
            0xd6565e3e = 0xfb464669
            0x46d2dfd3 = 0x7aec926c
            0x6d78ac72 = 0x24ca90ae
            0xd2c8fa6f = 0x80f20a4e
            0xbe6a7615 = 0x20985cf1
            0x9852d67e = 0xb3ec588d
            0x4543e999 = 0xd247c037
            0xead3c256 = 0xa8a2e850
            0xacf17fa8 = 0xd847c9a9
            0x338f637d = 0xa3a36918
            0xb9c9d361 = 0x91fdca46
            0x243e81b6 = 0x756c3c19
            0xac47b4f2 = 0xf8ac9aad
            0xc65b4dee = 0xa0167183
            0x4a8e6c32 = 0x86355129
            0x19f2b094 = 0xa0f5ecab
            0xd68d8ea4 = 0xe7cf3bd7
            0x3190c9e3 = 0x36563962
            0xb64e604f = 0xaae45ee8
            0x34aeb891 = 0x84d569be
            0x631db25c = 0xfc21073f
            0x173ad995 = 0xfd2108d2
            0x8aa39859 = 0xcfbc62f6
            0xf26df310 = 0xde0c199b
            0x54310ad9 = 0x92fe4f30
            0xdd587971 = 0x3ffae78c
            0xf475415d = 0x7bd58e3e
            0xf7bec269 = 0x4b6bb85c
            0x1877a055 = 0x1c89efca
            0x9291ddb9 = 0xb88f41a0
            0xed60495a = 0xea32ed93
            0xf39d67a6 = 0x52d0d053
            0x772825b8 = 0xf857ee67
            0x1571890e = 0xf0979017
            0xf7c7b804 = 0x473a84f5
            0x7cedf3f7 = 0x8c678c5a
            0x14b4d573 = 0x23ae91a4
            0xbeba5d20 = 0xcd5e1801
            0xc8cfc575 = 0x96ea13be
            0xbd1b28fe = 0x25a8139d
            0xdaebc7e8 = 0x2c89cf07
            0x59e92b92 = 0x58e6b683
            0xc66563b6 = 0x830cc9ad
            0x69331747 = 0x3b6487aa
            0x9985ed1d = 0x3ca13b30
            0xfab59416 = 0x111a93a1
            0x3fbfceed = 0xb3d31112
            0x55224c90 = 0xf9584389
            0x758cd1cd = 0x2001b666
            0xb6aebedb = 0x912d964e
            0x23212744 = 0x299f68b3
            0x0cfc4426 = 0x378034fb
            0x10fb4dc5 = 0xf61a11ba
            0xd322e342 = 0xe38720b5
            0x726fc1dd = 0x70a3f2a2
            0x70a6d0b4 = 0xc263d899
            0x89dff2d8 = 0x3085af3d
            0xf58b665e = 0x7172949d
            0xc13a080e = 0x3cdd23c7
            0xd79c150c = 0xb2e2a50f
            0xa1df443e = 0xa7ec95e3
            0xa0df42ab = 0xa8ec9776
            0xe476c6b0 = 0xd44e9e41
            0x18616224 = 0x80a7375d
            0x696305bc = 0x7887a8e5
            0xe776cb69 = 0xd14e9988
            0x465d832c = 0xb61717df
            0x05750559 = 0x04bcaff2
            0x2cbdc0be = 0x082d55c5
            0xf7e66ba1 = 0x51ac56f6
        }
    }
    0xfc4b9b02 = StaticMaterialDef {
        name: string = "Characters/Volibear/Skins/Skin21/Materials/InkTatoo_Hand_01_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "MatCap_Tex"
                texturePath: string = "ASSETS/Shared/Materials/MatCap_ToonPlastic.tex"
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "MatCap_Mask"
                texturePath: string = "ASSETS/Shared/Materials/gradient_a.tex"
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Diffuse_Texture"
                texturePath: string = "ASSETS/Characters/Udyr/Skins/Skin06/Udyr_Skin06_TattooMask_TX_CM.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Main_Texture"
                texturePath: string = "ASSETS/Characters/MasterYi/Skins/Skin89/MasterYi_Skin89_Tattoos_TX_CM.tex"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "OutlineMask_Texture"
                texturePath: string = "ASSETS/Shared/Materials/gradient_light_Dark.dds"
                addressU: u32 = 2
                addressV: u32 = 2
                addressW: u32 = 2
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Distortion_Diffuse_Tex_B_Control"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Distortion_Diffuse_Tex_RG_Control"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Distortion_Main_Tex_Control"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "MatCap_TintColor"
                value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "MatCap_Control"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "OutlineMask_Texture_B_UV"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollSpeedBase"
                value: vec4 = { 0, -0.400000006, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollSpeedBlend"
                value: vec4 = { 0, -0.129999995, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 1, 1, 1, 0.5 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Base_Tile"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Blend_Tile"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "BaseMat_Tint"
                value: vec4 = { 0.800000012, 0.270000011, 0.550000012, 2 }
            }
            StaticMaterialShaderParamDef {
                name: string = "BlendMat_Tint"
                value: vec4 = { 0, 0, 0, -0.5 }
            }
            StaticMaterialShaderParamDef {
                name: string = "MaskStrength"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "BloomValue"
            }
            StaticMaterialShaderParamDef {
                name: string = "OutlineColor"
                value: vec4 = { 0.701960802, 0, 0.00784313772, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "MainTex_TintColor"
                value: vec4 = { 1, 0.282352954, 0, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "OutlineControl"
            }
            StaticMaterialShaderParamDef {
                name: string = "OutlineMask_Strength"
            }
            StaticMaterialShaderParamDef {
                name: string = "WaveController"
                value: vec4 = { 15, 3, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "WaveStrength"
                value: vec4 = { 0, 0.75, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "AlphaClipValue"
            }
            StaticMaterialShaderParamDef {
                name: string = "AlphaClipNoiseStrength"
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_TintColor"
                value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "NoiseUV"
                value: vec4 = { 2, 2, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollSpeedMainTex"
            }
            StaticMaterialShaderParamDef {
                name: string = "MainTex_Tile"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Alpha_Control"
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "DISTORTION_DIFFUSE_TEX_RG"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DISTORTION_DIFFUSE_TEX_B"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DISTORTION_MAIN_TEX"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "MATCAP_ON"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_OUTLINEMASK_B_ALPHA"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "BLENDCOLOR_ON"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "ADDITIVEALPHA_ON"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "MASK_ON"
            }
            StaticMaterialSwitchDef {
                name: string = "MAINTEX_ON"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "OUTLINE_ON"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "OUTLINE_MASK_ON"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "ALPHABLEND_MAIN"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_MAINTEXCOLOR"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEFORM_ON"
            }
            StaticMaterialSwitchDef {
                name: string = "TWO_D_DEFORM_ON"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_MAINTEXALPHA"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "ALPHACLIP_ON"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "BLOOM_TINTCOLOR_ON"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "SCROLL_MAIN_TEX"
                on: bool = false
            }
        }
        shaderMacros: map[string,string] = {
            "NUM_BLEND_WEIGHTS" = "4"
        }
        techniques: list[embed] = {
            StaticMaterialTechniqueDef {
                name: string = "normal"
                passes: list[embed] = {
                    StaticMaterialPassDef {
                        shader: link = 0xead7a1f5
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                    }
                }
            }
        }
        childTechniques: list[embed] = {
            StaticMaterialChildTechniqueDef {
                name: string = "transition"
                parentName: string = "normal"
                shaderMacros: map[string,string] = {
                    "TRANSITION" = "1"
                }
            }
        }
    }
}
