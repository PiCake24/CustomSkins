#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Volibear_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6.bin"
    "DATA/Volibear_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin7_Skins_Skin9.bin"
    "DATA/Volibear_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin9.bin"
    "DATA/Characters/Volibear/Volibear.bin"
    "DATA/Characters/Volibear/Animations/Skin0.bin"
    "DATA/Volibear_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin9.bin"
    "DATA/Volibear_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5.bin"
    "DATA/Volibear_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin3_Skins_Skin5.bin"
}
entries: map[hash,embed] = {
    "Characters/Volibear/Skins/Skin3" = SkinCharacterDataProperties {
        skinClassification: u32 = 1
        championSkinName: string = "Runeguard Volibear"
        metaDataTags: string = "faction:freljord,gender:male,element:lightning,race:demigod,skinline:otherroads"
        skinUpgradeData: embed = skinUpgradeData {
            0xcb522723: list[link] = {
                0x70c00708
                0xf74bc37b
                0x113e43a6
                0xfc04cb75
            }
        }
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Characters/Volibear/Skins/Skin03/VolibearLoadscreen_3.tex"
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
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_Aura_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    0.400000006
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0399999991, 5 }
                }
                emitterName: string = "DarkAbove"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 20 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.0809399486
                            0.509138405
                            1
                        }
                        values: list[f32] = {
                            1
                            1
                            0
                            0
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    flags: u8 = 1
                    radius: f32 = 40
                    height: f32 = 25
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 40, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.184313729, 0.286274523, 0.505882382, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0984340012
                            0.482810736
                            1
                        }
                        values: list[vec4] = {
                            { 0.184313729, 0.286274523, 0.505882382, 0 }
                            { 0.184313729, 0.286274523, 0.505882382, 0.577943385 }
                            { 0.184313729, 0.286274523, 0.505882382, 1 }
                            { 0.184313729, 0.286274523, 0.505882382, 1 }
                        }
                    }
                }
                pass: i16 = 29
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                0.336353481
                                0.419168115
                                0.613982081
                                0.712234735
                                1
                            }
                            values: list[f32] = {
                                0
                                0.117647059
                                0.226890758
                                0.655462205
                                0.777076066
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 1.20000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
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
                    constantValue: vec3 = { 100, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0, 0 }
                            { 1, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Cas_Dust_01.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    0.600000024
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0199999996, 5 }
                }
                emitterName: string = "DarkGroundLayer"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 20 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.0809399486
                            0.509138405
                            1
                        }
                        values: list[f32] = {
                            1
                            1
                            0
                            0
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    flags: u8 = 1
                    radius: f32 = 10
                    height: f32 = 25
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.37000075, 0.420004576, 0.459998488, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.145413876
                            0.384376734
                            1
                        }
                        values: list[vec4] = {
                            { 0.37000075, 0.420004576, 0.459998488, 0 }
                            { 0.37000075, 0.420004576, 0.459998488, 0.640108168 }
                            { 0.37000075, 0.420004576, 0.459998488, 1 }
                            { 0.37000075, 0.420004576, 0.459998488, 1 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                0.336353481
                                0.419168115
                                0.613982081
                                0.712234735
                                1
                            }
                            values: list[f32] = {
                                0
                                0.117647059
                                0.226890758
                                0.655462205
                                0.777076066
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 1.20000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
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
                    constantValue: vec3 = { 100, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0, 0 }
                            { 1, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Cas_Dust_01.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.699999988
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.75
                        }
                    }
                }
                emitterName: string = "Masked_Static"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 20, 40, 20 }
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
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 20, 40, 20 }
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
                    constantValue: vec3 = { 0, 0, 50 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.450980395, 0.745098054, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0.450980395, 0.745098054, 1, 1 }
                            { 0.288273752, 0.476278365, 0.639215708, 1 }
                            { 0.245828524, 0.406151474, 0.545098066, 1 }
                        }
                    }
                }
                pass: i16 = 101
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
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
                                    0.49000001
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                    -90
                                    -90
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.653424621
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    0.65882355
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
                            { 80, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.699999988, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_tar_flipbook.dds"
                frameRate: f32 = 20
                numFrames: u16 = 9
                startFrame: u16 = 1
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 3, 3 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                particleLinger: option[f32] = {
                    0.400000006
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00999999978, 6 }
                }
                emitterName: string = "Shadow_"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 20 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.0809399486
                            0.509138405
                            1
                        }
                        values: list[f32] = {
                            1
                            1
                            0
                            0
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    flags: u8 = 1
                    radius: f32 = 20
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -150, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0899977088, 0.100007631, 0.110002287, 0.700007617 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.159268931
                            0.574879229
                            1
                        }
                        values: list[vec4] = {
                            { 0.0899977088, 0.100007631, 0.110002287, 0 }
                            { 0.0899977088, 0.100007631, 0.110002287, 0.700007617 }
                            { 0.0899977088, 0.100007631, 0.110002287, 0.700007617 }
                            { 0.0899977088, 0.100007631, 0.110002287, 0 }
                        }
                    }
                }
                pass: i16 = -1
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                0.535230577
                                0.8548522
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.827496231
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
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
                    constantValue: vec3 = { 150, 100, 100 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_ball32_02.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 4.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "innerLightning"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 20 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 20, 40, 20 }
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
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 20, 40, 20 }
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
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0235294122, 0.839215696, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0411943309
                            0.122950263
                            0.305344254
                            0.626744986
                            0.978873253
                        }
                        values: list[vec4] = {
                            { 0.0235294122, 0.839215696, 1, 0 }
                            { 0.0235294122, 0.839215696, 1, 1 }
                            { 0.0235294122, 0.839215696, 1, 0.894098341 }
                            { 0.0235294122, 0.839215696, 1, 0.501633227 }
                            { 0.0235294122, 0.839215696, 1, 0.157599941 }
                            { 0.0235294122, 0.839215696, 1, 0 }
                        }
                    }
                }
                pass: i16 = 40
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                0.357817292
                                0.5593431
                                0.782511711
                                0.998004675
                            }
                            values: list[f32] = {
                                0
                                0
                                0.502709866
                                0.888888896
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 100, 100 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Cas_Dust_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Ashe_Base_ground_CrackNoise_mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.109999999, 0.100000001 }
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
                                { 0.109999999, 0.100000001 }
                            }
                        }
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
                timeBeforeFirstEmission: f32 = 0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "Masked_Static1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 10, 40, 10 }
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
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 10, 40, 10 }
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
                    constantValue: vec3 = { 0, 0, 50 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.737254918, 0.866666675, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0.737254918, 0.866666675, 1, 1 }
                            { 0.471264899, 0.553986907, 0.639215708, 1 }
                            { 0.401876211, 0.472418308, 0.545098066, 1 }
                        }
                    }
                }
                pass: i16 = 101
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    -45
                                    45
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.49000001
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                    -90
                                    -90
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 80, 80 }
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
                            { 80, 80, 80 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_jacobsLadder.dds"
                frameRate: f32 = 16
                numFrames: u16 = 16
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 4, 4 }
            }
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
                emitterName: string = "glow"
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
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.607843161, 0.713725507, 1, 0.800000012 }
                }
                pass: i16 = 20
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionFeatherIn: f32 = 0.5
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Passive_Glow_A.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 0 }
                    fresnel: f32 = 0.100000001
                    fresnelColor: vec4 = { 0.0196078438, 0.313725501, 0.670588255, 1 }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_impactErode.dds"
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
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    2
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "bodyGradBlend1"
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
                    0x2fec8a25: flag = true
                    0x6b77a8ca: embed = ValueColor {
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0.00230946881
                                0.988452673
                            }
                            values: list[vec4] = {
                                { 1, 1, 1, 1 }
                                { 1, 1, 1, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.00999465957, 0.2399939, 0.319996953, 0.100007631 }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_R_Avatar_Blend_01.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.00999999978
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                particleLinger: option[f32] = {
                    0.400000006
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00999999978, 6 }
                }
                emitterName: string = "Softglow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 20 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    flags: u8 = 1
                    radius: f32 = 20
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.2399939, 0.730006874, 0.930006862, 0.100007631 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.159268931
                            0.574879229
                            1
                        }
                        values: list[vec4] = {
                            { 0.2399939, 0.730006874, 0.930006862, 0 }
                            { 0.2399939, 0.730006874, 0.930006862, 0.100007631 }
                            { 0.2399939, 0.730006874, 0.930006862, 0.100007631 }
                            { 0.2399939, 0.730006874, 0.930006862, 0 }
                        }
                    }
                }
                pass: i16 = 200
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
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
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Aura_Self.DDS"
            }
        }
        particleName: string = "Volibear_Skin03_Passive_maxStacks_Aura_01"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_Aura_01"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_E_AOE_Warning" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    2
                }
                emitterName: string = "DownWooshAdd"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -25, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Woosh_Pillar_A.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.500952363
                            0.613333344
                            0.706666648
                            0.801904798
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.0938596427 }
                            { 1, 1, 1, 0.292751849 }
                            { 1, 1, 1, 0.833187103 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 401
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.12382739
                                0.363977492
                                0.440900564
                                1
                            }
                            values: list[f32] = {
                                1
                                0.851851881
                                0.396825403
                                0
                                0
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.5
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_RuneBolt_B.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.5 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.200000003 }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.514285743
                            0.603809536
                            0.725714266
                            0.790476203
                            1
                        }
                        values: list[vec2] = {
                            { 0, 0 }
                            { 0, 0 }
                            { 0, 0 }
                            { 0, 0 }
                            { 0, 0 }
                            { 0, 0 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_lightningMist_01.dds"
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, -1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                0.514285743
                                0.603809536
                                0.725714266
                                0.790476203
                                1
                            }
                            values: list[vec2] = {
                                { 0, -0 }
                                { 0, -0.137566134 }
                                { 0, -0.291005284 }
                                { 0, -0.873015881 }
                                { 0, -1 }
                                { 0, -1 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    2
                }
                emitterName: string = "DownWooshBlend"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -25, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Woosh_Pillar_A.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.39000535, 0.200000003, 0.459998488, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.500952363
                            0.613333344
                            0.706666648
                            0.801904798
                            1
                        }
                        values: list[vec4] = {
                            { 0.39000535, 0.200000003, 0.459998488, 0 }
                            { 0.39000535, 0.200000003, 0.459998459, 0.0469305366 }
                            { 0.39000535, 0.200000003, 0.459998459, 0.14637816 }
                            { 0.39000535, 0.200000003, 0.459998488, 0.416599929 }
                            { 0.39000535, 0.200000003, 0.459998488, 0.500007629 }
                            { 0.39000535, 0.200000003, 0.459998488, 0.500007629 }
                        }
                    }
                }
                pass: i16 = 400
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.12382739
                                0.363977492
                                0.440900564
                                0.558161378
                                0.675422132
                                0.883677304
                                1
                            }
                            values: list[f32] = {
                                1
                                0.851851881
                                0.396825403
                                0
                                0
                                0.119212963
                                0.90625
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.5
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_RuneBolt_B.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.5 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.200000003 }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.514285743
                            0.603809536
                            0.725714266
                            0.790476203
                            1
                        }
                        values: list[vec2] = {
                            { 0, -0 }
                            { 0, -0.137566134 }
                            { 0, -0.291005284 }
                            { 0, -0.873015881 }
                            { 0, -1 }
                            { 0, -1 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.5 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_lightningMist_01.dds"
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, -4 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                0.514285743
                                0.603809536
                                0.725714266
                                0.790476203
                                1
                            }
                            values: list[vec2] = {
                                { 0, -0 }
                                { 0, -0.550264537 }
                                { 0, -1.16402113 }
                                { 0, -3.49206352 }
                                { 0, -4 }
                                { 0, -4 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 60
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.79999995
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
                            1.79999995
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterName: string = "Lightop"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -100, 250, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.50515461
                                    0.721649468
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.290090084
                                    0.863063037
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -100, 250, 0 }
                        }
                    }
                }
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -2400, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.0171428565
                            0.657425821
                            0.78142041
                            0.898797274
                            0.965714276
                        }
                        values: list[vec3] = {
                            { 0, 176.868759, 0 }
                            { 0, -101.43087, 0 }
                            { 0, -443.70578, 0 }
                            { 0, -1134.68152, 0 }
                            { 0, -2486.48657, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -200, 0 }
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
                            { 0, -200, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 1000, 50 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.899999976
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 50, 1000, 50 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.120462582
                            0.478095233
                            0.603809536
                            0.836190462
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.99999994, 0.99999994, 0.99999994, 0.85945946 }
                            { 1, 1, 1, 0.189189196 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 30
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                0.264552236
                                0.509566724
                                0.639990568
                                0.998004675
                            }
                            values: list[f32] = {
                                1
                                0.905405402
                                0.153153151
                                0
                                0
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.451428562
                            0.805714309
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.887387395, 0.887387395, 0.887387395 }
                            { 0.554054081, 0.554054081, 0.554054081 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_shield_ice_smoke.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Ashe_Skin03_ground_CrackNoise_mult.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.200000003, 0.200000003 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.109999999, 0.100000001 }
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
                                { 0.109999999, 0.100000001 }
                            }
                        }
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
                timeBeforeFirstEmission: f32 = 0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.304849893
                            0.494226336
                            1
                        }
                        values: list[f32] = {
                            0
                            8.37078667
                            11.9662924
                            15
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                lifetime: option[f32] = {
                    1.70000005
                }
                emitterName: string = "Static"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Static_Mesh_A.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.239770666
                            0.385681301
                            0.588914573
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0, 0.768627465, 1, 0.991342008 }
                            { 0, 0.751902044, 1, 0.461130142 }
                            { 0, 0.62999922, 1, 0.171777949 }
                            { 0, 0.349019617, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.0230946876
                                0.290875733
                                0.369488329
                                0.581794143
                                0.990762115
                            }
                            values: list[f32] = {
                                0
                                0
                                0.42696628
                                0.771535575
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Dissolve_Cloudy_01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 360, 0 }
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
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0.5, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
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
                        values: list[vec3] = {
                            { 1, 0.5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_RuneBolt_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.25 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 1 }
                        }
                    }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.258660495
                            0.381062359
                            1
                        }
                        values: list[vec2] = {
                            { 0, 0 }
                            { 0, 0 }
                            { 0, 0.200000003 }
                            { 0, 0.109363295 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0.5 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.29999995
                }
                particleLinger: option[f32] = {
                    2.70000005
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "WarningAddC"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, -5 }
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
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0477708653
                            0.568902612
                            0.80511421
                            0.877197444
                            0.95273304
                            1
                        }
                        values: list[vec4] = {
                            { 0.300007641, 0.190005347, 0.37000075, 0.189476743 }
                            { 0.144736841, 0.224996626, 0.409276605, 0.328853309 }
                            { 0.0699931309, 0.680003047, 0.919996977, 0.586107731 }
                            { 1, 1, 0.99999994, 0.800000012 }
                            { 0.529411793, 0.75686276, 1, 0.644649982 }
                            { 0.425674349, 0.62495935, 1, 0.385443091 }
                            { 0.371855706, 0.564359248, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.237494633
                                0.651050925
                                0.805337548
                                0.903664291
                                1
                            }
                            values: list[f32] = {
                                1
                                0.628502369
                                0.37895
                                0.206462607
                                0
                                0
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_AOE_Warning_B_Errode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 700, 600 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_AOE_Warning_B.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.79999995
                }
                particleLinger: option[f32] = {
                    2.79999995
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "WarningBlend"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.899290085
                            0.937919438
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.600000024 }
                            { 1, 1, 1, 0.50719142 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0591584519
                                0.167660832
                                0.304850489
                                0.475507736
                                1
                            }
                            values: list[f32] = {
                                1
                                0.759662569
                                0.408050239
                                0.16055046
                                0
                                0
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_AOE_Warning_B_Errode.dds"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 700, 600 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_AOE_Warning_A.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.79999995
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "WooshAdd"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Woosh_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.807843149, 0.450980395, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0761904791
                            0.13333334
                            0.19238095
                            0.249523804
                            0.867580175
                            0.95195514
                            1
                        }
                        values: list[vec4] = {
                            { 0.807843149, 0.450980395, 1, 0 }
                            { 0.807843149, 0.450980395, 1, 0.123185702 }
                            { 0.807843149, 0.450980395, 1, 0.366906464 }
                            { 0.807843149, 0.450980395, 1, 0.855105102 }
                            { 0.807843149, 0.450980395, 1, 0.985611498 }
                            { 0.807843149, 0.450980395, 1, 1 }
                            { 0.807843149, 0.450980395, 1, 0.860880136 }
                            { 0.807843149, 0.450980395, 1, 0 }
                        }
                    }
                }
                pass: i16 = 401
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.5 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_RuneSwipe.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 3 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 60
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.79999995
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
                            1.79999995
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterName: string = "darko"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1, 0 }
                        }
                    }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -100, 250, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.50515461
                                    0.721649468
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.290090084
                                    0.863063037
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { -100, 250, 0 }
                        }
                    }
                }
                velocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -2400, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.0171428565
                            0.657425821
                            0.78142041
                            0.898797274
                            0.965714276
                        }
                        values: list[vec3] = {
                            { 0, 176.868759, 0 }
                            { 0, -101.43087, 0 }
                            { 0, -443.70578, 0 }
                            { 0, -1134.68152, 0 }
                            { 0, -2486.48657, 0 }
                        }
                    }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -200, 0 }
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
                            { 0, -200, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 100, 800, 100 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.899999976
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 100, 800, 100 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.368627459, 0.419607848, 0.458823532, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.120462582
                            0.478095233
                            0.603809536
                            0.836190462
                            1
                        }
                        values: list[vec4] = {
                            { 0.368627459, 0.419607848, 0.458823532, 0 }
                            { 0.368627459, 0.419607848, 0.458823532, 1 }
                            { 0.368627459, 0.419607848, 0.458823532, 1 }
                            { 0.368627429, 0.419607818, 0.458823502, 0.85945946 }
                            { 0.368627459, 0.419607848, 0.458823532, 0.189189196 }
                            { 0.368627459, 0.419607848, 0.458823532, 0 }
                        }
                    }
                }
                pass: i16 = 20
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                0.264552236
                                0.509566724
                                0.639990568
                                0.998004675
                            }
                            values: list[f32] = {
                                1
                                0.905405402
                                0.153153151
                                0
                                0
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.451428562
                            0.805714309
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.887387395, 0.887387395, 0.887387395 }
                            { 0.554054081, 0.554054081, 0.554054081 }
                            { 0.100000001, 0.100000001, 0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_cas_trail_01.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Ashe_Skin03_ground_CrackNoise_mult.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.200000003, 0.200000003 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.109999999, 0.100000001 }
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
                                { 0.109999999, 0.100000001 }
                            }
                        }
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
                timeBeforeFirstEmission: f32 = 1.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "wooshAddB"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Woosh_B_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.509803951, 0.937254906, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.867580175
                            0.95195514
                            1
                        }
                        values: list[vec4] = {
                            { 0.509803951, 0.937254906, 1, 0 }
                            { 0.509803951, 0.937254906, 1, 1 }
                            { 0.509803951, 0.937254906, 1, 0.860880136 }
                            { 0.509803951, 0.937254906, 1, 0 }
                        }
                    }
                }
                pass: i16 = 401
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.5 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_RuneSwipe.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 3 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "wooshAddC"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 500, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Woosh_C_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.509803951, 0.937254906, 1, 0.501960814 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.867580175
                            0.95195514
                            1
                        }
                        values: list[vec4] = {
                            { 0.509803951, 0.937254906, 1, 0 }
                            { 0.509803951, 0.937254906, 1, 0.501960814 }
                            { 0.509803951, 0.937254906, 1, 0.432128072 }
                            { 0.509803951, 0.937254906, 1, 0 }
                        }
                    }
                }
                pass: i16 = 401
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.157598495
                                0.290806741
                                0.816135108
                                0.941838622
                                1
                            }
                            values: list[f32] = {
                                0
                                0.0675675645
                                0.184684679
                                0.882882893
                                1
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_SmokeErode.dds"
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.5, 1 }
                            { 0.5, 1, 0.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.25 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            -0.00190476188
                            0.405473411
                            0.684112847
                            0.844382763
                        }
                        values: list[vec2] = {
                            { 0, -0.009438009 }
                            { 0, -0.137446329 }
                            { 0, -0.49609068 }
                            { 0, -1.0476191 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_RuneSwipe.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 2 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.79999995
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "wooshBlend"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Woosh_01.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.220004573, 0.11999695, 0.269993126, 0.200000003 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0415704399
                            0.0704388022
                            0.867580175
                            0.95195514
                            1
                        }
                        values: list[vec4] = {
                            { 0.220004573, 0.11999695, 0.269993126, 0 }
                            { 0.220004573, 0.11999695, 0.269993126, 0.17489177 }
                            { 0.220004573, 0.11999695, 0.269993126, 0.200000003 }
                            { 0.220004573, 0.11999695, 0.269993126, 0.200000003 }
                            { 0.220004573, 0.11999695, 0.269993126, 0.172176018 }
                            { 0.220004573, 0.11999695, 0.269993126, 0 }
                        }
                    }
                }
                pass: i16 = 400
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.5 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_RuneSwipe.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 3 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                }
                particleLinger: option[f32] = {
                    2
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "wooshBlendB"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Woosh_B_01.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.220004573, 0.11999695, 0.269993126, 0.400000006 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.867580175
                            0.95195514
                            1
                        }
                        values: list[vec4] = {
                            { 0.220004573, 0.11999695, 0.269993126, 0 }
                            { 0.220004573, 0.11999695, 0.269993126, 0.400000006 }
                            { 0.220004573, 0.11999695, 0.269993126, 0.344352037 }
                            { 0.220004573, 0.11999695, 0.269993126, 0 }
                        }
                    }
                }
                pass: i16 = 400
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.5 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_RuneSwipe.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 3 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    2
                }
                emitterName: string = "DownWooshAdd1"
                disabled: bool = true
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -25, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Woosh_Pillar_A.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.500952363
                            0.613333344
                            0.706666648
                            0.801904798
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.0938596427 }
                            { 1, 1, 1, 0.292751849 }
                            { 1, 1, 1, 0.833187103 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 401
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.12382739
                                0.363977492
                                0.440900564
                                0.558161378
                                0.675422132
                                0.883677304
                                1
                            }
                            values: list[f32] = {
                                1
                                0.851851881
                                0.396825403
                                0
                                0
                                0.119212963
                                0.90625
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.5
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_RuneBolt_B.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.5 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.200000003 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.514285743
                            0.603809536
                            0.725714266
                            0.790476203
                            1
                        }
                        values: list[vec2] = {
                            { 0, -0 }
                            { 0, -0.275132269 }
                            { 0, -0.582010567 }
                            { 0, -1.74603176 }
                            { 0, -2 }
                            { 0, -2 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 2 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_lightningMist_01.dds"
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, -4 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                0.514285743
                                0.603809536
                                0.725714266
                                0.790476203
                                1
                            }
                            values: list[vec2] = {
                                { 0, -0 }
                                { 0, -0.550264537 }
                                { 0, -1.16402113 }
                                { 0, -3.49206352 }
                                { 0, -4 }
                                { 0, -4 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.20000005
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    2
                }
                emitterName: string = "DownWooshBlend1"
                disabled: bool = true
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -25, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Woosh_Pillar_A.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.39000535, 0.200000003, 0.459998488, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.500952363
                            0.613333344
                            0.706666648
                            0.801904798
                            1
                        }
                        values: list[vec4] = {
                            { 0.39000535, 0.200000003, 0.459998488, 0 }
                            { 0.39000535, 0.200000003, 0.459998459, 0.0938596427 }
                            { 0.39000535, 0.200000003, 0.459998459, 0.292751849 }
                            { 0.39000535, 0.200000003, 0.459998488, 0.833187103 }
                            { 0.39000535, 0.200000003, 0.459998488, 1 }
                            { 0.39000535, 0.200000003, 0.459998488, 1 }
                        }
                    }
                }
                pass: i16 = 400
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.12382739
                                0.363977492
                                0.440900564
                                0.558161378
                                0.675422132
                                0.883677304
                                1
                            }
                            values: list[f32] = {
                                1
                                0.851851881
                                0.396825403
                                0
                                0
                                0.119212963
                                0.90625
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.5
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_RuneBolt_B.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.5 }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.200000003 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.514285743
                            0.603809536
                            0.725714266
                            0.790476203
                            1
                        }
                        values: list[vec2] = {
                            { 0, -0 }
                            { 0, -0.275132269 }
                            { 0, -0.582010567 }
                            { 0, -1.74603176 }
                            { 0, -2 }
                            { 0, -2 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_lightningMist_01.dds"
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, -4 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                0.514285743
                                0.603809536
                                0.725714266
                                0.790476203
                                1
                            }
                            values: list[vec2] = {
                                { 0, -0 }
                                { 0, -0.550264537 }
                                { 0, -1.16402113 }
                                { 0, -3.49206352 }
                                { 0, -4 }
                                { 0, -4 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 1 }
                            }
                        }
                    }
                }
            }
        }
        particleName: string = "Volibear_Skin03_E_AOE_Warning"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_E_AOE_Warning"
        soundPersistentDefault: string = "Play_sfx_Volibear_VolibearE_buffactivate"
        flags: u16 = 214
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_R_SpikeB" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_midStacks_R_SpikeB"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_R_SpikeB"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_R_SpikeC" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_midStacks_R_SpikeC"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_R_SpikeC"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_R_SpikeA" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_midStacks_R_SpikeA"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_R_SpikeA"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_Aura_01" = VfxSystemDefinitionData {
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
                emitterName: string = "Avatar2"
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
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.270588249, 0.31764707, 1, 0.501960814 }
                }
                pass: i16 = 20
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionFeatherIn: f32 = 0.5
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Passive_Glow_A.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 0 }
                    fresnel: f32 = 0.100000001
                    fresnelColor: vec4 = { 0.0196078438, 0.313725501, 0.670588255, 1 }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_impactErode.dds"
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
                    constantValue: f32 = 0.00999999978
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                particleLinger: option[f32] = {
                    0.400000006
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00999999978, 6 }
                }
                emitterName: string = "Softglow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 20 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    flags: u8 = 1
                    radius: f32 = 20
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.654901981, 0.933333337, 0.0980392173 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.159268931
                            0.574879229
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.654901981, 0.933333337, 0 }
                            { 0, 0.654901981, 0.933333337, 0.0980392173 }
                            { 0, 0.654901981, 0.933333337, 0.0980392173 }
                            { 0, 0.654901981, 0.933333337, 0 }
                        }
                    }
                }
                pass: i16 = 200
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
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
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Aura_Self.DDS"
            }
        }
        particleName: string = "Volibear_Skin03_Passive_midStacks_Aura_01"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_Aura_01"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_BasicAttack_Swipe_R_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
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
                    0.25
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh2"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Attack_Swipe_BasicAttack_01.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0470588244, 0.309803933, 0.360784322, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0300230943
                            0.0681293309
                            0.286374122
                            0.778290987
                            1
                        }
                        values: list[vec4] = {
                            { 0.0470588244, 0.309803933, 0.360784322, 0 }
                            { 0.0470588244, 0.309803933, 0.360784322, 0.909090936 }
                            { 0.0470588244, 0.309803933, 0.360784322, 1 }
                            { 0.0470588244, 0.309803933, 0.360784322, 0.909284055 }
                            { 0.0470588244, 0.309803933, 0.360784322, 0.155844152 }
                            { 0.0470588244, 0.309803933, 0.360784322, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2.20000005 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "scratchAdd"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Attack_Swipe_BasicAttack_02.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0334872976
                            0.380776346
                            0.609699786
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.468856633, 0.854188919, 1, 1 }
                            { 0, 0.754021406, 1, 0.900007606 }
                            { 0, 0.646600485, 0.850522041, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.157043874
                                0.575057745
                                1
                            }
                            values: list[f32] = {
                                0
                                0.280898869
                                0.76404494
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Dissolve_Cloudy_01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Slash_B.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -3.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.115473442
                            0.237875283
                            0.360277146
                            1
                        }
                        values: list[vec2] = {
                            { 0, -3.20000005 }
                            { 0, -3.20000005 }
                            { 0, -1.55616713 }
                            { 0, -0.969439864 }
                            { 0, -0.251685381 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 1 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Scratch.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
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
                    0.25
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh5"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Attack_Swipe_BasicAttack_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0300230943
                            0.0681293309
                            0.286374122
                            0.778290987
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.454552382 }
                            { 1, 1, 1, 0.500007629 }
                            { 1, 1, 1, 0.454648942 }
                            { 1, 1, 1, 0.0779232681 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2.20000005 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_Wisp_Mult.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.5, 8 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
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
                    0.25
                }
                isSingleParticle: flag = true
                emitterName: string = "RuneSwipe"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Attack_Swipe_BasicAttack_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0300230943
                            0.0681293309
                            0.286374122
                            0.778290987
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.272734195 }
                            { 1, 1, 1, 0.300007641 }
                            { 1, 1, 1, 0.272792131 }
                            { 1, 1, 1, 0.0467544347 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2.20000005 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_RuneSwipe.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 4 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
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
                    0.25
                }
                isSingleParticle: flag = true
                emitterName: string = "RuneSwipe1"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Attack_Swipe_BasicAttack_01.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0313725509, 0.168627456, 0.254901975, 0.501960814 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0300230943
                            0.0681293309
                            0.286374122
                            0.778290987
                            1
                        }
                        values: list[vec4] = {
                            { 0.0313725509, 0.168627456, 0.254901975, 0 }
                            { 0.0313725509, 0.168627456, 0.254901975, 0.456327975 }
                            { 0.0313725509, 0.168627456, 0.254901975, 0.501960814 }
                            { 0.0313725509, 0.168627456, 0.254901975, 0.456424922 }
                            { 0.0313725509, 0.168627456, 0.254901975, 0.0782276541 }
                            { 0.0313725509, 0.168627456, 0.254901975, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2.20000005 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_RuneSwipe.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 4 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
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
                    0.25
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh6"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Attack_Swipe_BasicAttack_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0300230943
                            0.0681293309
                            0.286374122
                            0.778290987
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.909090936 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.909284055 }
                            { 1, 1, 1, 0.155844152 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 4
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_swipe_B.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.100000001 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2.20000005 }
                        }
                    }
                }
            }
        }
        particleName: string = "Volibear_Skin03_BasicAttack_Swipe_R_01"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_BasicAttack_Swipe_R_01"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_W_Marked_Scratch" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 7.9000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                particleLinger: option[f32] = {
                    0.400000006
                }
                lifetime: option[f32] = {
                    8.19999981
                }
                isSingleParticle: flag = true
                emitterName: string = "Endflash1"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 200, -5 }
                }
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_02.dds"
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0136363637
                            0.521029949
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 5
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1.5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1.5, 1.5, 1.5 }
                            { 0.75, 0.75, 0.75 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Flash_01.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    8
                }
                emitterName: string = "PoofsBlend2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -50, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 280, 0 }
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
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.497120917
                            0.69017154
                            0.89282167
                            1
                        }
                        values: list[vec4] = {
                            { 0.219607845, 0.325490206, 0.43921569, 0.800000012 }
                            { 0.392156869, 0.290196091, 0.482352942, 1 }
                            { 0.31764707, 0.278431386, 0.521568656, 1 }
                            { 0.352941185, 0.262745112, 0.458823532, 1 }
                            { 0, 0, 0, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.351724148
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                0.361624479
                                0.591268003
                                1
                            }
                            values: list[f32] = {
                                0
                                0.531178474
                                0.801855206
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1.20000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Cas_Dust_01.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.400000006
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0.0076530613
                            0.482474238
                            0.69653374
                            0.987628877
                        }
                        values: list[f32] = {
                            1.45522392
                            1.74626863
                            2.12686563
                            3.0447762
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0.016494846
                            0.512432754
                            0.802163899
                            1.00412369
                        }
                        values: list[f32] = {
                            0.726119399
                            0.678948522
                            0.333158821
                            0.271641791
                        }
                    }
                }
                lifetime: option[f32] = {
                    8
                }
                emitterName: string = "X_Heartbeat_A1"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 250, -5 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00400000019
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.451735824
                            0.570625901
                            0.948750019
                            1
                        }
                        values: list[vec4] = {
                            { 0.00999465957, 0.900007606, 1, 0.800000012 }
                            { 0.494117647, 0.501960814, 1, 1 }
                            { 1, 0, 0.0200045779, 1 }
                            { 1, 0.501960814, 0, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.105386414
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0, 0.0156862754, 0.501960814 }
                            { 1, 1, 1, 1 }
                            { 1, 0, 0.784313738, 0.501960814 }
                        }
                    }
                }
                pass: i16 = 2
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 100, 30 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.60000002, 1.60000002, 1.60000002 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Marked_X_01.dds"
                startFrame: u16 = 1
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Marked_X_Wiggle.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                0.800000012
                                1
                            }
                            values: list[vec2] = {
                                { 0, -0 }
                                { 0, -1 }
                                { 0, -1 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 1 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.400000006
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0.0076530613
                            0.482474238
                            0.69653374
                            0.987628877
                        }
                        values: list[f32] = {
                            1.45522392
                            1.74626863
                            2.12686563
                            3.0447762
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0.016494846
                            0.512432754
                            0.802163899
                            1.00412369
                        }
                        values: list[f32] = {
                            0.726119399
                            0.678948522
                            0.333158821
                            0.271641791
                        }
                    }
                }
                lifetime: option[f32] = {
                    8
                }
                emitterName: string = "X_Heartbeat_Bq1"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 250, -5 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00400000019
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.451735824
                            0.570625901
                            0.923749983
                            1
                        }
                        values: list[vec4] = {
                            { 0.00999465957, 0.900007606, 1, 0.800000012 }
                            { 0.494117647, 0.501960814, 1, 1 }
                            { 1, 0, 0.0200045779, 1 }
                            { 1, 0.407843143, 0.0117647061, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.105386414
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0, 0.0156862754, 0.501960814 }
                            { 1, 1, 1, 1 }
                            { 1, 0, 0.784313738, 0.501960814 }
                        }
                    }
                }
                pass: i16 = 2
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -35, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 70, 30 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.60000002, 1.60000002, 1.60000002 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Marked_X_01.dds"
                startFrame: u16 = 1
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Marked_X_Wiggle.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                0.800000012
                                1
                            }
                            values: list[vec2] = {
                                { 0, -0 }
                                { 0, -1 }
                                { 0, -1 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 1 }
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
                isSingleParticle: flag = true
                emitterName: string = "X_Slash_A1"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 250, -5 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00400000019
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.475409836
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0, 0.149019614, 1 }
                            { 1, 0.31764707, 0, 1 }
                            { 1, 0, 0.0666666701, 0 }
                        }
                    }
                }
                pass: i16 = 4
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 100, 30 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.60000002, 1.60000002, 1.60000002 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Marked_X_01.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 7, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Marked_02.dds"
                    texAddressModeMult: u8 = 2
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, -4 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, -4 }
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
                isSingleParticle: flag = true
                emitterName: string = "X_Slash_BB1"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 250, -5 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00400000019
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.475409836
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0, 0.149019614, 1 }
                            { 1, 0.31764707, 0, 1 }
                            { 1, 0, 0.0666666701, 0 }
                        }
                    }
                }
                pass: i16 = 4
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -35, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 70, 30 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.60000002, 1.60000002, 1.60000002 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Marked_X_01.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Marked_02.dds"
                    texAddressModeMult: u8 = 2
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, -4 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, -4 }
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
                    constantValue: f32 = 8
                }
                isSingleParticle: flag = true
                emitterName: string = "black2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 250, 0 }
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
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_12.dds"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.360784322, 0.360784322, 0.360784322, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0882917494
                            0.181609198
                            0.499040306
                            0.656429946
                            0.963531673
                            1
                        }
                        values: list[vec4] = {
                            { 0.104698196, 0.104698196, 0.104698196, 0 }
                            { 0.00424452126, 0.131580159, 0.16695118, 0.450980395 }
                            { 0.121676281, 0.137239531, 0.176855057, 1 }
                            { 0.00848904252, 0.158462137, 0.207981557, 1 }
                            { 0.360784322, 0.0155632449, 0.0608381405, 1 }
                            { 0.309850067, 0.343806237, 0, 1 }
                            { 0.360784322, 0.360784322, 0.360784322, 0 }
                        }
                    }
                }
                pass: i16 = 1
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_R_Background.dds"
            }
            VfxEmitterDefinitionData {
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
                emitterName: string = "startflash1"
                importance: u8 = 2
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0xb2dcc7dc: embed = ValueVector3 {
                        constantValue: vec3 = { 1.5, 1.5, 1.5 }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 200, -5 }
                }
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_02.dds"
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0136363637
                            0.521029949
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 5
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.5, 0.5, 0.5 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Flash_01.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
            }
        }
        particleName: string = "Volibear_Skin03_W_Marked_Scratch"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_W_Marked_Scratch"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_R_Buf_Max" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 11.4499998
                }
                particleLinger: option[f32] = {
                    0.449999988
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "BodyBGDark"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.294117659, 0.509803951, 0.600000024, 1 }
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
                            { 0.294117659, 0.509803951, 0.600000024, 0 }
                            { 0.294117659, 0.509803951, 0.600000024, 1 }
                            { 0.294117659, 0.509803951, 0.600000024, 1 }
                            { 0.0911188051, 0.159938484, 0.289411753, 0.963855445 }
                            { 0.0726643577, 0.13394849, 0.190588236, 0.850980401 }
                            { 0.0319617577, 0.0613980703, 0.100496106, 0 }
                        }
                    }
                }
                meshRenderFlags: u8 = 0
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -1 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Ult_Clouds_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    0x056df716: u8 = 0
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 2 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 4, 0, 0 }
                            }
                        }
                    }
                    paletteCount: i32 = 16
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.0500000007 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Ult_Clouds_A.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.200000003 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 12
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                lifetime: option[f32] = {
                    12.5
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "EndFlash"
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x5e4d31b7: flag = true
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
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
                pass: i16 = 43
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/color-hold.DDS"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 12
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                particleLinger: option[f32] = {
                    0.800000012
                }
                lifetime: option[f32] = {
                    12.5
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "EndWisps"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 10 }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x5e4d31b7: flag = true
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            1
                            0
                        }
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
                primitive: pointer = VfxPrimitiveAttachedMesh {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0537598431
                            0.13113606
                            0.767000079
                            0.852826655
                            0.921222746
                            0.984782636
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.614457846 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.80865556 }
                            { 1, 1, 1, 0.234091043 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 44
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.12895377
                                0.540145993
                                0.739659369
                                1
                            }
                            values: list[f32] = {
                                0
                                0.0588235296
                                0.647058845
                                0.873949587
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Dissolve_Cloudy_01.dds"
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 0 }
                    fresnel: f32 = 0.100000001
                    fresnelColor: vec4 = { 0.666666687, 1, 1, 1 }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.158808932
                            0.450372219
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.1210084, 1.1210084, 1.1210084 }
                            { 1.26302516, 1.26302516, 1.26302516 }
                            { 1.39999998, 1.39999998, 1.39999998 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_R_Avatar_Blend_01.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 2, 0, 0 }
                            }
                        }
                    }
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "JumpFlat"
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
                    0x2fec8a25: flag = true
                    0x6b77a8ca: embed = ValueColor {
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0.00230946881
                                0.988452673
                            }
                            values: list[vec4] = {
                                { 1, 1, 1, 1 }
                                { 1, 1, 1, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.149019614, 0.847058833, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0206718352
                            0.789024174
                            0.7985394
                            0.869903386
                            0.979328156
                        }
                        values: list[vec4] = {
                            { 0.149019614, 0.847058833, 1, 1 }
                            { 0.149019614, 0.847058833, 1, 1 }
                            { 0.149019614, 0.847058833, 1, 0.481927723 }
                            { 0.149019614, 0.847058833, 1, 0.132530123 }
                            { 0.149019614, 0.847058833, 1, 0 }
                        }
                    }
                }
                pass: i16 = 98
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 0 }
                    fresnel: f32 = 0.0500000007
                    fresnelColor: vec4 = { 0, 0.819607854, 1, 1 }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Volibear_Skin03_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                lifetime: option[f32] = {
                    12
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0199999996, 5 }
                }
                emitterName: string = "Lightop"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 100 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.0809399486
                            0.509138405
                            1
                        }
                        values: list[f32] = {
                            1
                            1
                            0
                            0
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 20, 450, 30 }
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
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.102908276
                            0.304250568
                            0.455700666
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.156626508 }
                            { 1, 1, 1, 0.759464204 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 30
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                0.249401912
                                0.330224723
                                0.595388055
                                0.72749579
                                0.998004675
                            }
                            values: list[f32] = {
                                0
                                0.075630255
                                0.201680675
                                0.74640739
                                0.897292256
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_R_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0, 0 }
                            { 1, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_R_shield_ice_smoke.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Ashe_Skin03_ground_CrackNoise_mult.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.200000003, 0.200000003 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.109999999, 0.100000001 }
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
                                { 0.109999999, 0.100000001 }
                            }
                        }
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
                timeBeforeFirstEmission: f32 = 1.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.699999988
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.75
                        }
                    }
                }
                lifetime: option[f32] = {
                    12
                }
                period: option[f32] = {
                    12
                }
                timeActiveDuringPeriod: option[f32] = {
                    12
                }
                emitterName: string = "Masked_Static"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xba945ee1 {
                    flags: u8 = 1
                    0x23a0d95c: vec3 = { 100, 100, 100 }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 300, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.450980395, 0.745098054, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0.450980395, 0.745098054, 1, 1 }
                            { 0.288273752, 0.476278365, 0.639215708, 1 }
                            { 0.245828524, 0.406151474, 0.545098066, 1 }
                        }
                    }
                }
                pass: i16 = 101
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                stencilMode: u8 = 2
                stencilRef: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
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
                                    0.49000001
                                    0.5
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                    -90
                                    -90
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 125, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.800000012
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
                            { 125, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.699999988, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_R_tar_flipbook.dds"
                frameRate: f32 = 20
                numFrames: u16 = 9
                startFrame: u16 = 1
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 3, 3 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.800000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                particleLinger: option[f32] = {
                    0.400000006
                }
                lifetime: option[f32] = {
                    12
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.00999999978, 6 }
                }
                emitterName: string = "Shadow"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 100 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.0809399486
                            0.509138405
                            1
                        }
                        values: list[f32] = {
                            0.5
                            0.5
                            0
                            0
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 20, 0, 30 }
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
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0899977088, 0.100007631, 0.110002287, 0.700007617 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.159268931
                            0.574879229
                            1
                        }
                        values: list[vec4] = {
                            { 0.0899977088, 0.100007631, 0.110002287, 0 }
                            { 0.0899977088, 0.100007631, 0.110002287, 0.700007617 }
                            { 0.0899977088, 0.100007631, 0.110002287, 0.700007617 }
                            { 0.0899977088, 0.100007631, 0.110002287, 0 }
                        }
                    }
                }
                pass: i16 = -1
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                0.535230577
                                0.8548522
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.827496231
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_R_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRotationEnabled: flag = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 100, 100 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_ball32_02.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 2.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 6
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = 0x6d78ac72
                        }
                    }
                }
                emitterName: string = "StaticParent"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -15, 10 }
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
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.239770666
                            0.385681301
                            0.588914573
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0, 0.768627465, 1, 0.991342008 }
                            { 0, 0.751902044, 1, 0.461130142 }
                            { 0, 0.62999922, 1, 0.171777949 }
                            { 0, 0.349019617, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.0230946876
                                0.290875733
                                0.369488329
                                0.581794143
                                0.990762115
                            }
                            values: list[f32] = {
                                0
                                0
                                0.42696628
                                0.771535575
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Dissolve_Cloudy_01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
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
                                    -1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 180, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                frameRate: f32 = 4
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 1 }
                        }
                    }
                }
                texDiv: vec2 = { 4, 1 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.258660495
                            0.381062359
                            1
                        }
                        values: list[vec2] = {
                            { 0, 0 }
                            { 0, 0 }
                            { 0, 0.200000003 }
                            { 0, 0.109363295 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.14999998
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    2
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "Stencil_Mask"
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
                    0x2fec8a25: flag = true
                    0x6b77a8ca: embed = ValueColor {
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0.00230946881
                                0.988452673
                            }
                            values: list[vec4] = {
                                { 1, 1, 1, 1 }
                                { 1, 1, 1, 0 }
                            }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDrawAlways: list[hash] = {
                            0xd5977cbe
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                }
                pass: i16 = -1
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0490243956
                                0.117908008
                                0.878859878
                                0.942025065
                                1
                            }
                            values: list[f32] = {
                                1.03311253
                                0.198412344
                                0
                                0
                                0.19157055
                                1.03311253
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Dissolve_Cloudy_01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { 1, 1 }
                stencilMode: u8 = 1
                stencilRef: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_skin5_R_color-hold.dds"
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
                    0.449999988
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "bodyBlend_A"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
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
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.309803933, 0.313725501, 0.482352942, 0.963855445 }
                            { 0.247058824, 0.262745112, 0.31764707, 0.850980401 }
                            { 0.108669974, 0.120434679, 0.167493507, 0 }
                        }
                    }
                }
                pass: i16 = 40
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_R_Avatar_Blend_01.dds"
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
                    0.449999988
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "bodyFresnel_A"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
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
                            { 0, 0, 0, 0.963855445 }
                            { 0, 0, 0, 0.850980401 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 43
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = -1
                    }
                    erosionFeatherIn: f32 = 0.5
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_R_Avatar_Blend_01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 0 }
                    fresnel: f32 = 0.200000003
                    fresnelColor: vec4 = { 0.0901960805, 0.576470613, 1, 1 }
                }
                depthBiasFactors: vec2 = { -1, -6 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/color-hold.DDS"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 4, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Dissolve_Cloudy_01.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.200000003 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 2.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 4.5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    12
                }
                emitterName: string = "innerLightning"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 20 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 40, 200, 40 }
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
                                        0
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 40, 200, 40 }
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
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0235294122, 0.839215696, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0411943309
                            0.122950263
                            0.305344254
                            0.626744986
                            0.978873253
                        }
                        values: list[vec4] = {
                            { 0.0235294122, 0.839215696, 1, 0 }
                            { 0.0235294122, 0.839215696, 1, 1 }
                            { 0.0235294122, 0.839215696, 1, 0.894098341 }
                            { 0.0235294122, 0.839215696, 1, 0.501633227 }
                            { 0.0235294122, 0.839215696, 1, 0.157599941 }
                            { 0.0235294122, 0.839215696, 1, 0 }
                        }
                    }
                }
                pass: i16 = 40
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                0.357817292
                                0.5593431
                                0.782511711
                                0.998004675
                            }
                            values: list[f32] = {
                                0
                                0
                                0.502709866
                                0.888888896
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_R_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                stencilMode: u8 = 2
                stencilRef: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 100, 100 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_R_shield_ice_smoke.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Ashe_Skin03_ground_CrackNoise_mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.109999999, 0.100000001 }
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
                                { 0.109999999, 0.100000001 }
                            }
                        }
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
                timeBeforeFirstEmission: f32 = 1.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                particleLinger: option[f32] = {
                    0.400000006
                }
                lifetime: option[f32] = {
                    12
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.0199999996, 5 }
                }
                emitterName: string = "midMid"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 100 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.0809399486
                            0.509138405
                            1
                        }
                        values: list[f32] = {
                            1
                            1
                            0
                            0
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 20, 350, 30 }
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
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.43921569, 0.501960814, 0.549019635, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.102908276
                            0.304250568
                            0.455700666
                            1
                        }
                        values: list[vec4] = {
                            { 0.43921569, 0.501960814, 0.549019635, 0 }
                            { 0.43921569, 0.501960814, 0.549019635, 0.156626508 }
                            { 0.43921569, 0.501960814, 0.549019635, 0.759464204 }
                            { 0.43921569, 0.501960814, 0.549019635, 1 }
                            { 0.43921569, 0.501960814, 0.549019635, 1 }
                        }
                    }
                }
                pass: i16 = 29
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                0.249401912
                                0.330224723
                                0.595388055
                                0.72749579
                                0.998004675
                            }
                            values: list[f32] = {
                                0
                                0.075630255
                                0.201680675
                                0.74640739
                                0.897292256
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_R_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 220, 120, 120 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.800000012, 0, 0 }
                            { 1, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_R_shield_ice_smoke.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 3, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 11.4499998
                }
                particleLinger: option[f32] = {
                    0.449999988
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "bodyAdd_A1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.490196079, 0.909803927, 1, 1 }
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
                            { 0.490196079, 0.909803927, 1, 0 }
                            { 0.490196079, 0.909803927, 1, 1 }
                            { 0.490196079, 0.909803927, 1, 1 }
                            { 0.151864663, 0.285428673, 0.482352942, 0.963855445 }
                            { 0.121107265, 0.239046514, 0.31764707, 0.850980401 }
                            { 0.0532695949, 0.109571941, 0.167493507, 0 }
                        }
                    }
                }
                pass: i16 = 44
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.20000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Passive_Glow_A.dds"
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 0 }
                    fresnelColor: vec4 = { 0.482352942, 0.992156863, 1, 1 }
                }
                depthBiasFactors: vec2 = { -1, -7 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/color-hold.DDS"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 0, 0, 0 }
                            }
                        }
                    }
                    paletteCount: i32 = 16
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Ashe_Skin03_ground_CrackNoise_mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.200000003 }
                    }
                }
            }
        }
        particleName: string = "Volibear_Skin03_R_Buf_Max"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_R_Buf_Max"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_E_AOE" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                lifetime: option[f32] = {
                    0.349999994
                }
                isSingleParticle: flag = true
                emitterName: string = "DownwardLight"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -12000, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 1700, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00300000003
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.215686277, 0.568627477, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.500007629 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
                colorLookUpScales: vec2 = { 1, 0.800000012 }
                alphaRef: u8 = 0
                colorLookUpOffsets: vec2 = { 0, 0.300000012 }
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 1200, 1 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_E_Glow_01.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            15
                            30
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.5
                                    0.600000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                lifetime: option[f32] = {
                    1.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Embers"
                importance: u8 = 2
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "AnnieFrostFire"
                        "AnnieGoth"
                    }
                }
                birthOrbitalVelocity: embed = ValueVector3 {
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
                                    -0.5
                                    1
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
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 2000, 0 }
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
                            { 10, 2000, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 10, 10 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 500, 200, 0 }
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
                            { 500, 200, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 1, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        300
                                        300
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        5
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.952941179, 0.952941179, 0.952941179, 0.592156887 }
                            { 0.741176486, 0.741176486, 0.741176486, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                particleIsLocalOrientation: flag = true
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                        values: list[vec3] = {
                            { 360, 360, 360 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 850, 850, 850 }
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
                            1
                        }
                        values: list[vec3] = {
                            { 850, 850, 850 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 16, 6, 2 }
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
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 16, 6, 2 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_E_SandFlecks.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.903243542
                                    0.97096777
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.243697479
                                    0.507563055
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            2
                        }
                    }
                }
                lifetime: option[f32] = {
                    1.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Embers1"
                importance: u8 = 2
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "AnnieFrostFire"
                        "AnnieGoth"
                    }
                }
                birthOrbitalVelocity: embed = ValueVector3 {
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
                                    -0.5
                                    1
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
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 600, 200 }
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
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    -1
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
                        values: list[vec3] = {
                            { 0, 600, 200 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 1 }
                }
                acceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 0, 200 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    -1
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
                        values: list[vec3] = {
                            { 400, 0, 200 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
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
                                        0
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        0.628148973
                                        0.842982292
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        63.8655472
                                        170.588242
                                        600
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.819607854, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0064516128
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.819607854, 1, 0 }
                            { 0, 0.819607854, 1, 1 }
                            { 0, 0.819607854, 1, 1 }
                            { 0, 0.781038046, 0.952941179, 0.592156887 }
                            { 0, 0.607474029, 0.741176486, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                particleIsLocalOrientation: flag = true
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                        values: list[vec3] = {
                            { 360, 360, 360 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 850, 850, 850 }
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
                            1
                        }
                        values: list[vec3] = {
                            { 850, 850, 850 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 36, 6, 2 }
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
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 36, 6, 2 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.089859955
                            0.164765298
                            0.787011921
                            1
                        }
                        values: list[vec3] = {
                            { 12, 12, 12 }
                            { 2.80153084, 2.82700849, 2.82700849 }
                            { 1.21375418, 1.19102681, 1.19102681 }
                            { 0.429471612, 0.429471612, 0.429471612 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_glowspecks.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                lifetime: option[f32] = {
                    0.280000001
                }
                isSingleParticle: flag = true
                emitterName: string = "Flash"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 80, 0 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 1, 1, 0.800000012 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 9
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
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
                                    0
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
                    constantValue: vec3 = { 350, 350, 350 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.300000012, 0.300000012, 0.300000012 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Star_Flash.dds"
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
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "GLowWipeIn"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 3, -5 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.142586336
                            0.381560296
                            0.611347497
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.65882355 }
                            { 0.0901960805, 0.68235296, 1, 0.274509817 }
                            { 0.0549019612, 0.431372553, 1, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.199664429
                                1
                            }
                            values: list[f32] = {
                                -1
                                0.203539819
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 1.29999995
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_E_AOE_Warning_B_Errode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 700, 600 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_E_AOE_Crater_Add_01.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0500000007
                rate: embed = ValueFloat {
                    constantValue: f32 = 200
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            0
                            200
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.5
                                    0.600000024
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            3
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                emitterName: string = "GlowWipeOut"
                importance: u8 = 2
                0xf50b1a41: pointer = 0xf4e37e07 {
                    keywordsExcluded: list[string] = {
                        "AnnieFrostFire"
                        "AnnieGoth"
                    }
                }
                birthOrbitalVelocity: embed = ValueVector3 {
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
                                    -0.5
                                    1
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
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 200, 0 }
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
                            { 50, 200, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 20 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 300, 100, 0 }
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
                            { 300, 100, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 1, 1 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        150
                                        325
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0
                                        5
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            180
                                            -180
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                    0.193996757
                                    0.743804574
                                    1
                                }
                                values: list[f32] = {
                                    1
                                    0.670270264
                                    0.335135132
                                    0
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -100, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
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
                                    0.400000006
                                    0.800000012
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.209994659, 0.209994659, 0.209994659, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.386090219
                            0.828195512
                            0.992481232
                        }
                        values: list[vec4] = {
                            { 0.209994659, 0.209994659, 0.209994659, 0 }
                            { 0.209994659, 0.209994659, 0.209994659, 1 }
                            { 0.209994659, 0.209994659, 0.209994659, 1 }
                            { 0.209994659, 0.209994659, 0.209994659, 0 }
                        }
                    }
                }
                pass: i16 = 1
                colorLookUpTypeY: u8 = 3
                particleIsLocalOrientation: flag = true
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                        values: list[vec3] = {
                            { 360, 360, 360 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 850, 850, 850 }
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
                            1
                        }
                        values: list[vec3] = {
                            { 850, 850, 850 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 26, 6, 2 }
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
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 26, 6, 2 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Flake.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "Lightning_Downward"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -25, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 400, 0 }
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
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.984313726, 1, 1 }
                            { 0.454901963, 0.270588249, 0.921568632, 1 }
                            { 0.788235307, 0.945098042, 1, 1 }
                        }
                    }
                }
                pass: i16 = 6
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0500000007
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_E_skyBolt_Erode_01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 2000, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.699999988, 0.5, 0.699999988 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_E_skyBolt_01.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -1 }
                }
                texAddressModeBase: u8 = 2
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_E_skyBolt_01.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
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
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "Lightning_erode_"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -25, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.300007641 }
                            { 1, 1, 1, 0.300007641 }
                        }
                    }
                }
                pass: i16 = 4
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0500000007
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.600000024
                    erosionFeatherOut: f32 = 0.600000024
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_impactErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 2000, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1.20000005, 1, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 6, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.5 }
                }
                texAddressModeBase: u8 = 2
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 2 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_E_skyBolt_01.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -0.200000003 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "Lightning_erode_1"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -25, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -200, 0 }
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
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.111864753
                            0.372164845
                            1
                        }
                        values: list[vec4] = {
                            { 0.836274505, 1, 1, 1 }
                            { 0.00833333377, 0.144607842, 1, 1 }
                            { 0.360784322, 0.59803921, 1, 1 }
                            { 1, 0.988235295, 0.984313726, 1 }
                        }
                    }
                }
                pass: i16 = 5
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0537523441
                                0.180112571
                                0.390354931
                                0.732928693
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.560509562
                                0.885987282
                                1
                                1.10000002
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_E_skyBolt_Erode_01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 350, 2200, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.949999988, 0.99000001, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                texAddressModeBase: u8 = 2
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 2 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_E_skyBolt_01.dds"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 60
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.463439912
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.931818187
                                    1.20000005
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.200000003
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Shockwave"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1800, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    0
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1800, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1.5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 15, 0 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                                        1
                                        1
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 15, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 360
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            0.800000012
                                            0.800999999
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0.25
                                            0.899999976
                                            0.100000001
                                            0.0500000007
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    360
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.158861578
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.647058845, 0.894117653, 1, 1 }
                            { 0.443137258, 0.87843138, 0.996078432, 0 }
                        }
                    }
                }
                pass: i16 = -52
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 90, 1 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.386666656
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.386999995
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.386999995
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.600000024
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 200, 200, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.226498261
                            0.480825961
                            1
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0, 0 }
                            { 0.430649698, 0.632476568, 0 }
                            { 0.334710747, 0.858938277, 0 }
                            { 0.325619847, 1, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Nova.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
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
                            { 0, 0 }
                        }
                    }
                }
                texAddressModeBase: u8 = 2
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Dissolve_Cloudy_01.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.200000003, 0.200000003 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 2 }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 1000 }
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
                                { 1, 1000 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
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
                particleLinger: option[f32] = {
                    0.300000012
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "SnowFlash"
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.800000012
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.200000003
                                    0.800000012
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.0470588244, 0.792156875, 0.996078432, 1 }
                            { 0.380392164, 0.419607848, 1, 0 }
                        }
                    }
                }
                pass: i16 = -20
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 0 }
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
                            { 90, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 280, 700, 600 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 280, 700, 600 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.238747418
                            0.358747423
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.834884942, 0, 0 }
                            { 1.13342869, 0, 0 }
                            { 1.5, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Crit_hit_erode.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "SnowFlash1"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 20, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0, 0.831372559, 0.996078432, 1 }
                            { 0, 0.533333361, 1, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 0 }
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
                            { 90, 1, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 700, 600 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Flash_01.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 20
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
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
                            1
                        }
                    }
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                emitterName: string = "blast"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 0, 400 }
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    12
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
                            { 400, 0, 400 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 15, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    radius: f32 = 60
                    height: f32 = 1
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.76000613, 0.689997733, 0.530006886, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.76000613, 0.689997733, 0.530006886, 0 }
                            { 0.76000613, 0.689997733, 0.530006886, 0.600000024 }
                            { 0.684011281, 0.621003211, 0.47701022, 0.401995867 }
                            { 0.76000613, 0.689997733, 0.530006886, 0 }
                        }
                    }
                }
                pass: i16 = -150
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 1.20000005
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.150000006
                                1
                            }
                            values: list[f32] = {
                                0
                                1.20000005
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.70000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 90, 0 }
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
                            { 1, 90, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 50, 1, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 1, 1 }
                            { 1, 2, 2 }
                            { 1.5, 1.5, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Cas_Dust_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "flash1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 40, 0 }
                }
                0x4ffce322: pointer = 0xb13097f0 {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                    scaleEmitOffsetByBoundObjectSize: f32 = 0.00499999989
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.776470602 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                useNavmeshMask: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 0, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 360, 0, 1 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 300, 300 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Star_Flash.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.913333297
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    0.600000024
                                    1.20000005
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
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "shards"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1200, 1600, 300 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    -1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.25
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
                        values: list[vec3] = {
                            { 1200, 1600, 300 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1.5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -1600, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -1600, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                                { 0, 0, 0 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 360
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            0.800000012
                                            0.800999999
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            0.25
                                            0.899999976
                                            0.100000001
                                            0.0500000007
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    360
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 10, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.218125954
                            0.859248281
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.329411775, 0.843137264, 1, 1 }
                            { 0.179995418, 0.39000535, 1, 1 }
                            { 0.0313725509, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = -51
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    180
                                    -180
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 3, 3, 3 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.800000012
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    0.699999988
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 30, 30 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_flying_shards.dds"
                numFrames: u16 = 16
                birthUvScrollRate: embed = ValueVector2 {
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
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
                            { 0, 0 }
                        }
                    }
                }
                texDiv: vec2 = { 4, 4 }
                textureMult: pointer = 0xb097c1bd {
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.100000001, -0.100000001 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "wipeInCrater"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 3, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.829999208, 0.829999208, 0.829999208, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0731975436
                            0.16948393
                            0.350176126
                            0.607233107
                            1
                        }
                        values: list[vec4] = {
                            { 0.829999208, 0.829999208, 0.829999208, 1 }
                            { 0.829999208, 0.829999208, 0.829999208, 1 }
                            { 0.793314159, 0.793314159, 0.793314159, 0.721668959 }
                            { 0.498051941, 0.49330911, 0.49330911, 0.390256047 }
                            { 0.226268142, 0.226268142, 0.226268142, 0.132569045 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = -1
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0439272821
                                0.175260916
                                0.511714756
                                0.81087476
                                1
                            }
                            values: list[f32] = {
                                0
                                0.13171947
                                0.351921827
                                0.488333821
                                0.601209104
                                0.754716992
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0
                    erosionSliceWidth: f32 = 1.20000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_E_AOE_Warning_B_Errode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 700, 600 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_E_AOE_Crater_Blend_01.dds"
            }
        }
        particleName: string = "Volibear_Skin03_E_AOE"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_E_AOE"
        soundOnCreateDefault: string = "Play_sfx_Volibear_VolibearE_explo"
        flags: u16 = 198
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_W_Marked" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_W_Marked"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_W_Marked"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_Rock_A" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 8
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                lifetime: option[f32] = {
                    8.5
                }
                emitterName: string = "Add1"
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
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.601482213
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.489997715 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 250, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.243827164
                            0.658950627
                            1
                        }
                        values: list[vec3] = {
                            { 1.01339281, 1.01339281, 1.01339281 }
                            { 0.53125, 0.53125, 0.53125 }
                            { 0.0803571418, 0.0803571418, 0.0803571418 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_flareblue.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 8
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                lifetime: option[f32] = {
                    8.5
                }
                emitterName: string = "Embers"
                importance: u8 = 2
                birthOrbitalVelocity: embed = ValueVector3 {
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
                                    -0.5
                                    1
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
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.0809399486
                            0.509138405
                            1
                        }
                        values: list[f32] = {
                            0.5
                            0.5
                            0
                            0
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
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
                                        80
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        100
                                        200
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.952941179, 0.952941179, 0.952941179, 0.592156887 }
                            { 0.741176486, 0.741176486, 0.741176486, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                        values: list[vec3] = {
                            { 360, 360, 360 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 850, 850, 850 }
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
                            1
                        }
                        values: list[vec3] = {
                            { 850, 850, 850 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 6, 2 }
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
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 6, 2 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_SandFlecks.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8.19999981
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_Rock_A.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.141649053
                            0.983165801
                            1
                        }
                        values: list[vec4] = {
                            { 0.0588235296, 0.235294119, 0.239215687, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.00392156886, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.150476187
                                0.967592597
                                0.987654328
                            }
                            values: list[f32] = {
                                1
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1.20000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStoneErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                isRotationEnabled: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0.100000001, 2, -0.100000001 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.118000001
                            0.257192373
                            0.733371496
                            0.832371473
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, -0 }
                            { 0, 0, -0 }
                            { 0.0130391298, 0.260782599, -0.0130391298 }
                            { 0.0922173932, 1.84434783, -0.0922173932 }
                            { 0.100000001, 2, -0.100000001 }
                            { 0.100000001, 2, -0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStone.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 2
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                lifetime: option[f32] = {
                    8
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 40 }
                }
                emitterName: string = "Trail_Add"
                translationOverride: vec3 = { 0, -50, 0 }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 50 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x2fec8a25: flag = true
                    0x6b77a8ca: embed = ValueColor {
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.988913536
                            }
                            values: list[vec4] = {
                                { 1, 1, 1, 1 }
                                { 1, 1, 1, 0 }
                            }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -20, 40, 0 }
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
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 1200
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 1200, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                        mMaxAddedPerFrame: i32 = 20
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0414343365
                            0.679662347
                            0.988913536
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0644716099
                            0.491207451
                            0.712201297
                            0.820125401
                            0.993348122
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.0534767509 }
                            { 1, 1, 1, 0.422466338 }
                            { 0.400000006, 0.889356136, 1, 0.500007629 }
                            { 0.253978491, 0.781291485, 0.99999994, 0.387706459 }
                            { 0.0196078438, 0.607843161, 1, 0 }
                        }
                    }
                }
                pass: i16 = 7
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.00416666688
                                0.0340848826
                                0.0686587319
                                0.212852359
                                0.329558581
                                0.448607117
                                0.73809278
                                0.89187187
                                1
                            }
                            values: list[f32] = {
                                1
                                0.192660555
                                0
                                0
                                0.0964958817
                                0.251495808
                                0.771866262
                                0.938431442
                                1
                            }
                        }
                    }
                    0x26b4e623: bool = true
                    0x7d4f3ccc: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.163817286
                                0.227353469
                                0.444331706
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.485074639
                                0.931862414
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.600000024
                    erosionFeatherOut: f32 = 0.600000024
                    erosionMapName: string = "ASSETS/Characters/Senna/Skins/Base/Particles/Senna_Base_AutoAttack_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.159671038
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_recall_RuneTrail.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                emitterUvScrollRate: vec2 = { -0.5, 0 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 2
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                lifetime: option[f32] = {
                    8
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 40 }
                }
                emitterName: string = "Trail_Blendo"
                translationOverride: vec3 = { 0, -50, 0 }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 50 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x2fec8a25: flag = true
                    0x6b77a8ca: embed = ValueColor {
                        constantValue: vec4 = { 0.121568628, 0.521568656, 0.717647076, 1 }
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.988913536
                            }
                            values: list[vec4] = {
                                { 0.121568628, 0.521568656, 0.717647076, 1 }
                                { 0.121568628, 0.521568656, 0.717647076, 0 }
                            }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -20, 40, 0 }
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
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 1200
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 1200, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                        mMaxAddedPerFrame: i32 = 20
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0414343365
                            0.679662347
                            0.988913536
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.100007631, 0.429999232, 0.600000024, 0.400000006 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.187461659
                            0.548466384
                            0.993348122
                        }
                        values: list[vec4] = {
                            { 0.100007631, 0.429999232, 0.600000024, 0 }
                            { 0.100007631, 0.429999232, 0.599999964, 0.400000006 }
                            { 0.100007631, 0.429999232, 0.600000024, 0.400000006 }
                            { 0.100007631, 0.429999232, 0.600000024, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.00416666688
                                0.0340848826
                                0.0686587319
                                0.212852359
                                0.329558581
                                0.448607117
                                0.73809278
                                0.89187187
                                1
                            }
                            values: list[f32] = {
                                1
                                0.192660555
                                0
                                0
                                0.0964958817
                                0.251495808
                                0.771866262
                                0.938431442
                                1
                            }
                        }
                    }
                    0x26b4e623: bool = true
                    0x7d4f3ccc: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.163817286
                                0.227353469
                                0.444331706
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.485074639
                                0.931862414
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.600000024
                    erosionFeatherOut: f32 = 0.600000024
                    erosionMapName: string = "ASSETS/Characters/Senna/Skins/Base/Particles/Senna_Base_AutoAttack_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.159671038
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_recall_RuneTrail.dds"
                emitterUvScrollRate: vec2 = { -0.5, 0 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 8
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                lifetime: option[f32] = {
                    8.5
                }
                emitterName: string = "endgeoflash"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_Rock_A.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0810731798
                            0.185185179
                            0.44135803
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.541065454 }
                            { 1, 1, 1, 0.165545598 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 6
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.134567767
                                0.486501068
                                0.745457888
                                0.993359923
                            }
                            values: list[f32] = {
                                0
                                0
                                0.174107149
                                0.473214298
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1.20000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStoneErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 1 }
                    fresnelColor: vec4 = { 0, 0.86999315, 1, 1 }
                }
                isRotationEnabled: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0.100000001, 2, -0.100000001 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.118000001
                            0.257192373
                            0.733371496
                            0.832371473
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, -0 }
                            { 0, 0, -0 }
                            { 0.0130391298, 0.260782599, -0.0130391298 }
                            { 0.0922173932, 1.84434783, -0.0922173932 }
                            { 0.100000001, 2, -0.100000001 }
                            { 0.100000001, 2, -0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStone.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    0x34d8fac6: embed = ValueFloat {
                        constantValue: f32 = 2
                    }
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Add2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 20, 0 }
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
                    constantValue: vec4 = { 0, 0.450003803, 0.620004594, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0498915389
                            0.0780911073
                            0.121272929
                            0.935438454
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.450003803, 0.620004594, 0 }
                            { 0, 0.450003803, 0.620004594, 0.124726579 }
                            { 0, 0.450003803, 0.620004594, 0.697821021 }
                            { 0, 0.450003803, 0.620004594, 0.800000012 }
                            { 0, 0.450003803, 0.620004594, 0.800000012 }
                            { 0, 0.450003803, 0.620004594, 0 }
                        }
                    }
                }
                pass: i16 = 5
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 130, 160, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0605042018
                            0.122689076
                            0.929411769
                            0.982646406
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.804255307, 0.804255307, 0.804255307 }
                            { 0.995744705, 1, 1 }
                            { 1, 1, 1 }
                            { 0.897872329, 0.897872329, 0.897872329 }
                            { 0.710638285, 0.727659583, 0.727659583 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_ball32_02.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Blend"
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
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.00392156886, 0.192156866, 0.270588249, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0498915389
                            0.0780911073
                            0.121272929
                            0.935438454
                            1
                        }
                        values: list[vec4] = {
                            { 0.00392156886, 0.192156866, 0.270588249, 0 }
                            { 0.00392156886, 0.192156866, 0.270588249, 0.155908227 }
                            { 0.00392156886, 0.192156866, 0.270588249, 0.872276247 }
                            { 0.00392156886, 0.192156866, 0.270588249, 1 }
                            { 0.00392156886, 0.192156866, 0.270588249, 1 }
                            { 0.00392156886, 0.192156866, 0.270588249, 0 }
                        }
                    }
                }
                pass: i16 = -1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 250, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0605042018
                            0.122689076
                            0.929411769
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.804255307, 0.804255307, 0.804255307 }
                            { 0.995744705, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_ball32_02.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8.19999981
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_Rock_A.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.141649053
                            0.869978845
                            1
                        }
                        values: list[vec4] = {
                            { 0.0588235296, 0.235294119, 0.239215687, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = -1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0796019882
                                0.21846956
                                1
                            }
                            values: list[f32] = {
                                -1
                                -1
                                -0
                                -0
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStoneErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                isRotationEnabled: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0.100000001, 2, -0.100000001 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.118000001
                            0.257192373
                            0.733371496
                            0.832371473
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, -0 }
                            { 0, 0, -0 }
                            { 0.0130391298, 0.260782599, -0.0130391298 }
                            { 0.0922173932, 1.84434783, -0.0922173932 }
                            { 0.100000001, 2, -0.100000001 }
                            { 0.100000001, 2, -0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStone_Add.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Tornado_Indicator_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1 }
                    }
                }
            }
        }
        particleName: string = "Volibear_Skin03_Recall_Rock_A"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_Rock_A"
        flags: u16 = 197
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_Rock_C" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8.19999981
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_Rock_C.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.141649053
                            0.983165801
                            1
                        }
                        values: list[vec4] = {
                            { 0.0588235296, 0.235294119, 0.239215687, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.00392156886, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.150476187
                                0.967592597
                                0.987654328
                            }
                            values: list[f32] = {
                                1
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1.20000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStoneErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                isRotationEnabled: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0.100000001, 1.5, -0.100000001 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.118000001
                            0.257192373
                            0.733371496
                            0.832371473
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, -0 }
                            { 0, 0, -0 }
                            { 0.0130391298, 0.19558695, -0.0130391298 }
                            { 0.0922173932, 1.38326085, -0.0922173932 }
                            { 0.100000001, 1.5, -0.100000001 }
                            { 0.100000001, 1.5, -0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStone.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8.19999981
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_Rock_C.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.141649053
                            0.869978845
                            1
                        }
                        values: list[vec4] = {
                            { 0.0588235296, 0.235294119, 0.239215687, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = -1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.150476187
                                1
                            }
                            values: list[f32] = {
                                -1
                                -0
                                -0
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStoneErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                isRotationEnabled: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0.100000001, 1.5, -0.100000001 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.118000001
                            0.257192373
                            0.733371496
                            0.832371473
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, -0 }
                            { 0, 0, -0 }
                            { 0.0130391298, 0.19558695, -0.0130391298 }
                            { 0.0922173932, 1.38326085, -0.0922173932 }
                            { 0.100000001, 1.5, -0.100000001 }
                            { 0.100000001, 1.5, -0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStone_Add.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Tornado_Indicator_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 8
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                lifetime: option[f32] = {
                    8.5
                }
                emitterName: string = "endgeoflash"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_Rock_C.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0810731798
                            0.185185179
                            0.44135803
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.541065454 }
                            { 1, 1, 1, 0.165545598 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 6
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.134567767
                                0.486501068
                                0.745457888
                                0.993359923
                            }
                            values: list[f32] = {
                                0
                                0
                                0.174107149
                                0.473214298
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1.20000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStoneErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 1 }
                    fresnelColor: vec4 = { 0, 0.86999315, 1, 1 }
                }
                isRotationEnabled: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0.100000001, 1.5, -0.100000001 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.118000001
                            0.257192373
                            0.733371496
                            0.832371473
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, -0 }
                            { 0, 0, -0 }
                            { 0.0130391298, 0.19558695, -0.0130391298 }
                            { 0.0922173932, 1.38326085, -0.0922173932 }
                            { 0.100000001, 1.5, -0.100000001 }
                            { 0.100000001, 1.5, -0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStone.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    0x34d8fac6: embed = ValueFloat {
                        constantValue: f32 = 2
                    }
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 2
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                lifetime: option[f32] = {
                    8
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 40 }
                }
                emitterName: string = "Trail_Add"
                translationOverride: vec3 = { 0, -50, 0 }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 50 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x2fec8a25: flag = true
                    0x6b77a8ca: embed = ValueColor {
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.988913536
                            }
                            values: list[vec4] = {
                                { 1, 1, 1, 1 }
                                { 1, 1, 1, 0 }
                            }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -20, 40, 0 }
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
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 1200
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 1200, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                        mMaxAddedPerFrame: i32 = 20
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0414343365
                            0.679662347
                            0.988913536
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0644716099
                            0.491207451
                            0.712201297
                            0.820125401
                            0.993348122
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.0534767509 }
                            { 1, 1, 1, 0.422466338 }
                            { 0.400000006, 0.889356136, 1, 0.500007629 }
                            { 0.253978491, 0.781291485, 0.99999994, 0.387706459 }
                            { 0.0196078438, 0.607843161, 1, 0 }
                        }
                    }
                }
                pass: i16 = 7
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.00416666688
                                0.0340848826
                                0.0686587319
                                0.212852359
                                0.329558581
                                0.448607117
                                0.73809278
                                0.89187187
                                1
                            }
                            values: list[f32] = {
                                1
                                0.192660555
                                0
                                0
                                0.0964958817
                                0.251495808
                                0.771866262
                                0.938431442
                                1
                            }
                        }
                    }
                    0x26b4e623: bool = true
                    0x7d4f3ccc: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.163817286
                                0.227353469
                                0.444331706
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.485074639
                                0.931862414
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.600000024
                    erosionFeatherOut: f32 = 0.600000024
                    erosionMapName: string = "ASSETS/Characters/Senna/Skins/Base/Particles/Senna_Base_AutoAttack_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.159671038
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_recall_RuneTrail.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                emitterUvScrollRate: vec2 = { -0.5, 0 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 2
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                lifetime: option[f32] = {
                    8
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 40 }
                }
                emitterName: string = "Trail_Blendo"
                translationOverride: vec3 = { 0, -50, 0 }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 50 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x2fec8a25: flag = true
                    0x6b77a8ca: embed = ValueColor {
                        constantValue: vec4 = { 0.121568628, 0.521568656, 0.717647076, 1 }
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.988913536
                            }
                            values: list[vec4] = {
                                { 0.121568628, 0.521568656, 0.717647076, 1 }
                                { 0.121568628, 0.521568656, 0.717647076, 0 }
                            }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -20, 40, 0 }
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
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 1200
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 1200, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                        mMaxAddedPerFrame: i32 = 20
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0414343365
                            0.679662347
                            0.988913536
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.100007631, 0.429999232, 0.600000024, 0.400000006 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.187461659
                            0.548466384
                            0.993348122
                        }
                        values: list[vec4] = {
                            { 0.100007631, 0.429999232, 0.600000024, 0 }
                            { 0.100007631, 0.429999232, 0.599999964, 0.400000006 }
                            { 0.100007631, 0.429999232, 0.600000024, 0.400000006 }
                            { 0.100007631, 0.429999232, 0.600000024, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.00416666688
                                0.0340848826
                                0.0686587319
                                0.212852359
                                0.329558581
                                0.448607117
                                0.73809278
                                0.89187187
                                1
                            }
                            values: list[f32] = {
                                1
                                0.192660555
                                0
                                0
                                0.0964958817
                                0.251495808
                                0.771866262
                                0.938431442
                                1
                            }
                        }
                    }
                    0x26b4e623: bool = true
                    0x7d4f3ccc: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.163817286
                                0.227353469
                                0.444331706
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.485074639
                                0.931862414
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.600000024
                    erosionFeatherOut: f32 = 0.600000024
                    erosionMapName: string = "ASSETS/Characters/Senna/Skins/Base/Particles/Senna_Base_AutoAttack_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.159671038
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_recall_RuneTrail.dds"
                emitterUvScrollRate: vec2 = { -0.5, 0 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 8
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                lifetime: option[f32] = {
                    8.5
                }
                emitterName: string = "Add1"
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
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.601482213
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.489997715 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 250, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.243827164
                            0.658950627
                            1
                        }
                        values: list[vec3] = {
                            { 1.01339281, 1.01339281, 1.01339281 }
                            { 0.53125, 0.53125, 0.53125 }
                            { 0.0803571418, 0.0803571418, 0.0803571418 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_flareblue.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 8
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                lifetime: option[f32] = {
                    8.5
                }
                emitterName: string = "Embers"
                importance: u8 = 2
                birthOrbitalVelocity: embed = ValueVector3 {
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
                                    -0.5
                                    1
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
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.0809399486
                            0.509138405
                            1
                        }
                        values: list[f32] = {
                            0.5
                            0.5
                            0
                            0
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
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
                                        80
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        100
                                        200
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.952941179, 0.952941179, 0.952941179, 0.592156887 }
                            { 0.741176486, 0.741176486, 0.741176486, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                        values: list[vec3] = {
                            { 360, 360, 360 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 850, 850, 850 }
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
                            1
                        }
                        values: list[vec3] = {
                            { 850, 850, 850 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 6, 2 }
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
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 6, 2 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_SandFlecks.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Add2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 20, 0 }
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
                    constantValue: vec4 = { 0, 0.450003803, 0.620004594, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0498915389
                            0.0780911073
                            0.121272929
                            0.935438454
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.450003803, 0.620004594, 0 }
                            { 0, 0.450003803, 0.620004594, 0.124726579 }
                            { 0, 0.450003803, 0.620004594, 0.697821021 }
                            { 0, 0.450003803, 0.620004594, 0.800000012 }
                            { 0, 0.450003803, 0.620004594, 0.800000012 }
                            { 0, 0.450003803, 0.620004594, 0 }
                        }
                    }
                }
                pass: i16 = 5
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 130, 160, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0605042018
                            0.122689076
                            0.929411769
                            0.982646406
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.804255307, 0.804255307, 0.804255307 }
                            { 0.995744705, 1, 1 }
                            { 1, 1, 1 }
                            { 0.897872329, 0.897872329, 0.897872329 }
                            { 0.710638285, 0.727659583, 0.727659583 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_ball32_02.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Blend"
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
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.00392156886, 0.192156866, 0.270588249, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0498915389
                            0.0780911073
                            0.121272929
                            0.935438454
                            1
                        }
                        values: list[vec4] = {
                            { 0.00392156886, 0.192156866, 0.270588249, 0 }
                            { 0.00392156886, 0.192156866, 0.270588249, 0.155908227 }
                            { 0.00392156886, 0.192156866, 0.270588249, 0.872276247 }
                            { 0.00392156886, 0.192156866, 0.270588249, 1 }
                            { 0.00392156886, 0.192156866, 0.270588249, 1 }
                            { 0.00392156886, 0.192156866, 0.270588249, 0 }
                        }
                    }
                }
                pass: i16 = -1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 250, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0605042018
                            0.122689076
                            0.929411769
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.804255307, 0.804255307, 0.804255307 }
                            { 0.995744705, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_ball32_02.dds"
            }
        }
        particleName: string = "Volibear_Skin03_Recall_Rock_C"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_Rock_C"
        flags: u16 = 197
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_Rock_B" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Add"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 20, 0 }
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
                    constantValue: vec4 = { 0, 0.450003803, 0.620004594, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0498915389
                            0.0780911073
                            0.121272929
                            0.935438454
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.450003803, 0.620004594, 0 }
                            { 0, 0.450003803, 0.620004594, 0.124726579 }
                            { 0, 0.450003803, 0.620004594, 0.697821021 }
                            { 0, 0.450003803, 0.620004594, 0.800000012 }
                            { 0, 0.450003803, 0.620004594, 0.800000012 }
                            { 0, 0.450003803, 0.620004594, 0 }
                        }
                    }
                }
                pass: i16 = 5
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 130, 160, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0605042018
                            0.122689076
                            0.929411769
                            0.982646406
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.804255307, 0.804255307, 0.804255307 }
                            { 0.995744705, 1, 1 }
                            { 1, 1, 1 }
                            { 0.897872329, 0.897872329, 0.897872329 }
                            { 0.710638285, 0.727659583, 0.727659583 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_ball32_02.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 8
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                lifetime: option[f32] = {
                    8.5
                }
                emitterName: string = "Add1"
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
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.601482213
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.489997715 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 250, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.243827164
                            0.658950627
                            1
                        }
                        values: list[vec3] = {
                            { 1.01339281, 1.01339281, 1.01339281 }
                            { 0.53125, 0.53125, 0.53125 }
                            { 0.0803571418, 0.0803571418, 0.0803571418 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_flareblue.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Blend"
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
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.00392156886, 0.192156866, 0.270588249, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0498915389
                            0.0780911073
                            0.121272929
                            0.935438454
                            1
                        }
                        values: list[vec4] = {
                            { 0.00392156886, 0.192156866, 0.270588249, 0 }
                            { 0.00392156886, 0.192156866, 0.270588249, 0.155908227 }
                            { 0.00392156886, 0.192156866, 0.270588249, 0.872276247 }
                            { 0.00392156886, 0.192156866, 0.270588249, 1 }
                            { 0.00392156886, 0.192156866, 0.270588249, 1 }
                            { 0.00392156886, 0.192156866, 0.270588249, 0 }
                        }
                    }
                }
                pass: i16 = -1
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 250, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0605042018
                            0.122689076
                            0.929411769
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0.804255307, 0.804255307, 0.804255307 }
                            { 0.995744705, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_ball32_02.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 8
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                lifetime: option[f32] = {
                    8.5
                }
                emitterName: string = "Embers"
                importance: u8 = 2
                birthOrbitalVelocity: embed = ValueVector3 {
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
                                    -0.5
                                    1
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
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.0809399486
                            0.509138405
                            1
                        }
                        values: list[f32] = {
                            0.5
                            0.5
                            0
                            0
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
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
                                        80
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        100
                                        200
                                    }
                                }
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 1, 1, 1 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 1
                            dynamics: pointer = VfxAnimatedFloatVariableData {
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
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    1
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.400000006
                                    1
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.300000012
                                    1
                                }
                            }
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.952941179, 0.952941179, 0.952941179, 0.592156887 }
                            { 0.741176486, 0.741176486, 0.741176486, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                        values: list[vec3] = {
                            { 360, 360, 360 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 850, 850, 850 }
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
                            1
                        }
                        values: list[vec3] = {
                            { 850, 850, 850 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 6, 2 }
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
                                    0.699999988
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1
                                    2
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 20, 6, 2 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_SandFlecks.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8.19999981
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_Rock_B.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.141649053
                            0.983165801
                            1
                        }
                        values: list[vec4] = {
                            { 0.0588235296, 0.235294119, 0.239215687, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.00392156886, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.150476187
                                0.967592597
                                0.987654328
                            }
                            values: list[f32] = {
                                1
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1.20000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStoneErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                isRotationEnabled: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0.100000001, 0.5, -0.100000001 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.118000001
                            0.257192373
                            0.733371496
                            0.832371473
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, -0 }
                            { 0, 0, -0 }
                            { 0.0130391298, 0.0651956499, -0.0130391298 }
                            { 0.0922173932, 0.461086959, -0.0922173932 }
                            { 0.100000001, 0.5, -0.100000001 }
                            { 0.100000001, 0.5, -0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStone.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 8.19999981
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_Rock_B.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.141649053
                            0.869978845
                            1
                        }
                        values: list[vec4] = {
                            { 0.0588235296, 0.235294119, 0.239215687, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = -1
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.150476187
                                1
                            }
                            values: list[f32] = {
                                -1
                                -0
                                -0
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStoneErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                isRotationEnabled: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0.100000001, 0.5, -0.100000001 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.118000001
                            0.257192373
                            0.733371496
                            0.832371473
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, -0 }
                            { 0, 0, -0 }
                            { 0.0130391298, 0.0651956499, -0.0130391298 }
                            { 0.0922173932, 0.461086959, -0.0922173932 }
                            { 0.100000001, 0.5, -0.100000001 }
                            { 0.100000001, 0.5, -0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStone_Add.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_E_Tornado_Indicator_Mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 2
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                lifetime: option[f32] = {
                    8
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 40 }
                }
                emitterName: string = "Trail_Add"
                translationOverride: vec3 = { 0, -50, 0 }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 50 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x2fec8a25: flag = true
                    0x6b77a8ca: embed = ValueColor {
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.988913536
                            }
                            values: list[vec4] = {
                                { 1, 1, 1, 1 }
                                { 1, 1, 1, 0 }
                            }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -20, 40, 0 }
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
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 1200
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 1200, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                        mMaxAddedPerFrame: i32 = 20
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0414343365
                            0.679662347
                            0.988913536
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0644716099
                            0.491207451
                            0.712201297
                            0.820125401
                            0.993348122
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.0534767509 }
                            { 1, 1, 1, 0.422466338 }
                            { 0.400000006, 0.889356136, 1, 0.500007629 }
                            { 0.253978491, 0.781291485, 0.99999994, 0.387706459 }
                            { 0.0196078438, 0.607843161, 1, 0 }
                        }
                    }
                }
                pass: i16 = 7
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.00416666688
                                0.0340848826
                                0.0686587319
                                0.212852359
                                0.329558581
                                0.448607117
                                0.73809278
                                0.89187187
                                1
                            }
                            values: list[f32] = {
                                1
                                0.192660555
                                0
                                0
                                0.0964958817
                                0.251495808
                                0.771866262
                                0.938431442
                                1
                            }
                        }
                    }
                    0x26b4e623: bool = true
                    0x7d4f3ccc: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.163817286
                                0.227353469
                                0.444331706
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.485074639
                                0.931862414
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.600000024
                    erosionFeatherOut: f32 = 0.600000024
                    erosionMapName: string = "ASSETS/Characters/Senna/Skins/Base/Particles/Senna_Base_AutoAttack_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.159671038
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_recall_RuneTrail.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                emitterUvScrollRate: vec2 = { -0.5, 0 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 2
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                lifetime: option[f32] = {
                    8
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 40 }
                }
                emitterName: string = "Trail_Blendo"
                translationOverride: vec3 = { 0, -50, 0 }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 50 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x2fec8a25: flag = true
                    0x6b77a8ca: embed = ValueColor {
                        constantValue: vec4 = { 0.121568628, 0.521568656, 0.717647076, 1 }
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.988913536
                            }
                            values: list[vec4] = {
                                { 0.121568628, 0.521568656, 0.717647076, 1 }
                                { 0.121568628, 0.521568656, 0.717647076, 0 }
                            }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { -20, 40, 0 }
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
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 1200
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 1200, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                        mMaxAddedPerFrame: i32 = 20
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0414343365
                            0.679662347
                            0.988913536
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.100007631, 0.429999232, 0.600000024, 0.400000006 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.187461659
                            0.548466384
                            0.993348122
                        }
                        values: list[vec4] = {
                            { 0.100007631, 0.429999232, 0.600000024, 0 }
                            { 0.100007631, 0.429999232, 0.599999964, 0.400000006 }
                            { 0.100007631, 0.429999232, 0.600000024, 0.400000006 }
                            { 0.100007631, 0.429999232, 0.600000024, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.00416666688
                                0.0340848826
                                0.0686587319
                                0.212852359
                                0.329558581
                                0.448607117
                                0.73809278
                                0.89187187
                                1
                            }
                            values: list[f32] = {
                                1
                                0.192660555
                                0
                                0
                                0.0964958817
                                0.251495808
                                0.771866262
                                0.938431442
                                1
                            }
                        }
                    }
                    0x26b4e623: bool = true
                    0x7d4f3ccc: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.163817286
                                0.227353469
                                0.444331706
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.485074639
                                0.931862414
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.600000024
                    erosionFeatherOut: f32 = 0.600000024
                    erosionMapName: string = "ASSETS/Characters/Senna/Skins/Base/Particles/Senna_Base_AutoAttack_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.159671038
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_recall_RuneTrail.dds"
                emitterUvScrollRate: vec2 = { -0.5, 0 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 8
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                lifetime: option[f32] = {
                    8.5
                }
                emitterName: string = "endgeoflash"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_Rock_B.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0810731798
                            0.185185179
                            0.44135803
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.541065454 }
                            { 1, 1, 1, 0.165545598 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 6
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.134567767
                                0.486501068
                                0.745457888
                                0.993359923
                            }
                            values: list[f32] = {
                                0
                                0
                                0.174107149
                                0.473214298
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1.20000005
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStoneErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 1 }
                    fresnelColor: vec4 = { 0, 0.86999315, 1, 1 }
                }
                isRotationEnabled: flag = true
                isLocalOrientation: flag = false
                rotation0: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0.100000001, 2, -0.100000001 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.118000001
                            0.257192373
                            0.733371496
                            0.832371473
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, -0 }
                            { 0, 0, -0 }
                            { 0.0130391298, 0.260782599, -0.0130391298 }
                            { 0.0922173932, 1.84434783, -0.0922173932 }
                            { 0.100000001, 2, -0.100000001 }
                            { 0.100000001, 2, -0.100000001 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Recall_RuneStone.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    0x34d8fac6: embed = ValueFloat {
                        constantValue: f32 = 2
                    }
                    paletteCount: i32 = 16
                }
            }
        }
        particleName: string = "Volibear_Skin03_Recall_Rock_B"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_Rock_B"
        flags: u16 = 197
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_BasicAttack_Swipe_L_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
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
                    0.25
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh2"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Attack_Swipe_L_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0415704399
                            0.0704388022
                            0.457274824
                            0.778290987
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.4372361 }
                            { 1, 1, 1, 0.500007629 }
                            { 1, 1, 1, 0.500007629 }
                            { 1, 1, 1, 0.0779232681 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2.20000005 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_Wisp_Mult.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 2 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "scratchAdd"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Attack_Swipe_L_02.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0404157043
                            0.380776346
                            0.609699786
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.784670234, 1, 1, 1 }
                            { 0.468856633, 0.854188919, 1, 1 }
                            { 0, 0.754021406, 1, 0.900007606 }
                            { 0, 0.646600485, 0.850522041, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0739030018
                                0.307159364
                                0.702078521
                                1
                            }
                            values: list[f32] = {
                                0
                                0.209737822
                                0.6179775
                                0.902621746
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Dissolve_Cloudy_01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Slash_B.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -3.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.115473442
                            0.237875283
                            0.387990773
                            1
                        }
                        values: list[vec2] = {
                            { 0, -3.20000005 }
                            { 0, -3.20000005 }
                            { 0, -1.73284519 }
                            { 0, -0.958397508 }
                            { 0, -0.251685381 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 1 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Scratch.dds"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
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
                    0.25
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh5"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Attack_Swipe_L_01.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.180392161, 0.349019617, 0.454901963, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0300230943
                            0.0681293309
                            0.286374122
                            0.778290987
                            1
                        }
                        values: list[vec4] = {
                            { 0.180392161, 0.349019617, 0.454901963, 0 }
                            { 0.180392161, 0.349019617, 0.454901963, 0.909090936 }
                            { 0.180392161, 0.349019617, 0.454901963, 1 }
                            { 0.180392161, 0.349019617, 0.454901963, 0.909284055 }
                            { 0.180392161, 0.349019617, 0.454901963, 0.155844152 }
                            { 0.180392161, 0.349019617, 0.454901963, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2.20000005 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_RuneSwipe.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 2 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
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
                    0.25
                }
                isSingleParticle: flag = true
                emitterName: string = "RuneSwipe"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Attack_Swipe_L_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0300230943
                            0.0681293309
                            0.286374122
                            0.778290987
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.454552382 }
                            { 1, 1, 1, 0.500007629 }
                            { 1, 1, 1, 0.454648942 }
                            { 1, 1, 1, 0.0779232681 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2.20000005 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_RuneSwipe.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 8 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -0.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
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
                    0.25
                }
                isSingleParticle: flag = true
                emitterName: string = "RuneSwipe1"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Attack_Swipe_L_01.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0300230943
                            0.0681293309
                            0.286374122
                            0.778290987
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.454552382 }
                            { 1, 1, 1, 0.500007629 }
                            { 1, 1, 1, 0.454648942 }
                            { 1, 1, 1, 0.0779232681 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2.20000005 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_RuneSwipe.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 8 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -0.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
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
                    0.25
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh6"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Attack_Swipe_L_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.200000003 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0300230943
                            0.0681293309
                            0.286374122
                            0.778290987
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.181818187 }
                            { 1, 1, 1, 0.200000003 }
                            { 1, 1, 1, 0.181856811 }
                            { 1, 1, 1, 0.0311688315 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 3
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_Swipe_A.dds"
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2.20000005 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_RuneSwipe.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 2 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.200000003
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
                    0.25
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh7"
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Attack_Swipe_L_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0300230943
                            0.0681293309
                            0.286374122
                            0.778290987
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.909090936 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.909284055 }
                            { 1, 1, 1, 0.155844152 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 4
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_swipe_B.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.100000001 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2.20000005 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2.20000005 }
                        }
                    }
                }
            }
        }
        particleName: string = "Volibear_Skin03_BasicAttack_Swipe_L_01"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_BasicAttack_Swipe_L_01"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Q_floatyRunes" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.10000002
                }
                particleLinger: option[f32] = {
                    1.10000002
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "BAckBlend"
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
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_12.dds"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0549019612, 0.137254909, 0.262745112, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            -0.0103347898
                            0.765510678
                            0.983897924
                        }
                        values: list[vec4] = {
                            { 0.0549019612, 0.137254909, 0.262745112, 1 }
                            { 0.0549019612, 0.137254909, 0.262745112, 1 }
                            { 0.0549019612, 0.137254909, 0.262745112, 0 }
                        }
                    }
                }
                pass: i16 = -1
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.00416666688
                                0.212852359
                                0.316280812
                                0.435329348
                                0.663869202
                                0.817648292
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.16191645
                                0.401028514
                                0.809249461
                                0.975814641
                                1
                            }
                        }
                    }
                    0x26b4e623: bool = true
                    0x7d4f3ccc: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0785597414
                                0.22585924
                                1
                            }
                            values: list[f32] = {
                                0
                                0.489130437
                                0.782608688
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.600000024
                    erosionFeatherOut: f32 = 0.600000024
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Dissolve_Cloudy_01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_ball32_02.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    0.200000003
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Basic2"
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
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0279069766
                            0.400742114
                            0.990697682
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.00416666688
                                0.212852359
                                0.329558581
                                0.448607117
                                0.73809278
                                0.89187187
                                1
                            }
                            values: list[f32] = {
                                0.0470085479
                                0
                                0.0964958817
                                0.251495808
                                0.771866262
                                0.938431442
                                1
                            }
                        }
                    }
                    0x26b4e623: bool = true
                    0x7d4f3ccc: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0785597414
                                0.22585924
                                1
                            }
                            values: list[f32] = {
                                0
                                0.489130437
                                0.782608688
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.150000006
                    erosionFeatherOut: f32 = 0.150000006
                    erosionMapName: string = "ASSETS/Characters/Senna/Skins/Base/Particles/Senna_Base_AutoAttack_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 10, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Base_Runes_01.dds"
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
        }
        particleName: string = "Volibear_Skin03_Q_floatyRunes"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Q_floatyRunes"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_L_SpikeA" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_maxStacks_L_SpikeA"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_L_SpikeA"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_L_SpikeB" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_maxStacks_L_SpikeB"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_L_SpikeB"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_L_SpikeC" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_maxStacks_L_SpikeC"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_L_SpikeC"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_W_Slash" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.25
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "scratchAdd"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 600 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 1 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -150, -150 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_W_Slash_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0334712602
                            0.135405973
                            0.652777791
                            0.885162711
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.996078432, 0.862745106, 1, 0.972549021 }
                            { 1, 0, 0.768627465, 0.64508003 }
                            { 0.850980401, 0, 0.654901981, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -2 }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -10, -180, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0920000002
                            0.291000009
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 1, 1, 0.693000019 }
                            { 1, 1, 0.873000026 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_W_Slash_B.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -3.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.115473442
                            0.237875283
                            0.387990773
                            1
                        }
                        values: list[vec2] = {
                            { 0, -3.5 }
                            { 0, -3.5 }
                            { 0, -1.89529943 }
                            { 0, -1.04824722 }
                            { 0, -0.275280893 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 1 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_W_Scratch.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 4, 1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.25
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Swooshblend"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 600 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 1 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -150, -150 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_W_Slash_01.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.701960802, 0.360784322, 0.611764729, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0334712602
                            0.359943002
                            0.612014592
                            1
                        }
                        values: list[vec4] = {
                            { 0.701960802, 0.360784322, 0.611764729, 0 }
                            { 0.701960802, 0.360784322, 0.611764729, 1 }
                            { 0.701960802, 0.360784322, 0.611764729, 1 }
                            { 0, 0.334928095, 0.611764729, 0.900007606 }
                            { 0, 0.233283296, 0.520319343, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -10, -180, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0920000002
                            0.291000009
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 1, 1, 0.693000019 }
                            { 1, 1, 0.873000026 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_W_Slash_B.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 3.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.115473442
                            0.237875283
                            0.387990773
                            1
                        }
                        values: list[vec2] = {
                            { 0, 3.5 }
                            { 0, 3.5 }
                            { 0, 1.89529943 }
                            { 0, 1.04824722 }
                            { 0, 0.275280893 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 1 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.25
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "scratchAdd2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 600 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 1 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -150, -150 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_W_Slash_01.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0334712602
                            0.359943002
                            0.612014592
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0, 0.928333342, 1, 0.900007606 }
                            { 0, 0.646600485, 0.850522041, 0 }
                        }
                    }
                }
                pass: i16 = 3
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -10, -180, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0920000002
                            0.291000009
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 1, 1, 0.693000019 }
                            { 1, 1, 0.873000026 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_W_swipe_B.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.0500000007 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -3.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.115473442
                            0.237875283
                            0.387990773
                            1
                        }
                        values: list[vec2] = {
                            { 0, -3.5 }
                            { 0, -3.5 }
                            { 0, -1.89529943 }
                            { 0, -1.04824722 }
                            { 0, -0.275280893 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 1 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.25
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "scratchBlend"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 600 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 1 }
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -150, -150 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_W_Slash_01.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0334712602
                            0.135405973
                            0.652777791
                            0.885162711
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.996078432, 0.862745106, 1, 0.972549021 }
                            { 1, 0, 0.768627465, 0.64508003 }
                            { 0.850980401, 0, 0.654901981, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -2 }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -10, -180, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0920000002
                            0.291000009
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 0.5 }
                            { 1, 1, 0.693000019 }
                            { 1, 1, 0.873000026 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_W_Slash_B.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -3.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.115473442
                            0.237875283
                            0.387990773
                            1
                        }
                        values: list[vec2] = {
                            { 0, -3.5 }
                            { 0, -3.5 }
                            { 0, -1.89529943 }
                            { 0, -1.04824722 }
                            { 0, -0.275280893 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 1 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_W_Scratch.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 4, 1 }
                    }
                }
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
                emitterName: string = "flash"
                importance: u8 = 2
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 80, -250 }
                }
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_alpha_02.dds"
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0136363637
                            0.521029949
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.335746616, 0.508295655, 1, 1 }
                            { 0.0749622956, 0.286727011, 1, 1 }
                        }
                    }
                }
                pass: i16 = 15
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 200, 200 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.5, 0.5, 0.5 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Flash_01.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.25
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.505423009
                                    0.75921911
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.206363633
                                    0.49545455
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "flash1"
                importance: u8 = 2
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 80, -250 }
                }
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_alpha_02.dds"
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0136363637
                            0.521029949
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.335746616, 0.508295655, 1, 1 }
                            { 0.0749622956, 0.286727011, 1, 1 }
                        }
                    }
                }
                pass: i16 = 15
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 45, 0, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 200, 200 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0583174005
                            0.998087943
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.865671635, 0.871065319, 0.871065319 }
                            { 0.838215649, 0.838215649, 0.838215649 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_sparkMote.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 15, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "Volibear_Skin03_W_Slash"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_W_Slash"
        flags: u16 = 198
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_ThunderClap_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 8
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                lifetime: option[f32] = {
                    8.5
                }
                emitterName: string = "Add1"
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
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.601482213
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.489997715 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 250, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.243827164
                            0.658950627
                            1
                        }
                        values: list[vec3] = {
                            { 1.01339281, 1.01339281, 1.01339281 }
                            { 0.53125, 0.53125, 0.53125 }
                            { 0.0803571418, 0.0803571418, 0.0803571418 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_flareblue.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "Avatar"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.330006868, 0.800000012, 1, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.00129414455, 0.800000012, 1, 0.300007641 }
                            { 0.330006868, 0.800000012, 1, 0 }
                        }
                    }
                }
                pass: i16 = 19
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.505423009
                                    0.75921911
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.206363633
                                    0.49545455
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "flash"
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_12.dds"
                blendMode: u8 = 4
                pass: i16 = 1
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
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
                            { 90, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 100, 100 }
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
                            { 300, 100, 100 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_sparkMote.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "flash1"
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_12.dds"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0627451017, 0.529411793, 0.698039234, 1 }
                }
                meshRenderFlags: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0304761901
                                0.275377125
                                0.670278072
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.626332283
                                0.903448284
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
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
                            { 90, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.197231829
                            0.484429061
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 0.563636363, 0, 0 }
                            { 0.272727281, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Aura_Self.DDS"
            }
        }
        particleName: string = "Volibear_Skin03_Recall_ThunderClap_01"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_ThunderClap_01"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_ThunderClap_02" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 8
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                lifetime: option[f32] = {
                    8.5
                }
                emitterName: string = "Add1"
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
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.601482213
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.489997715 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 250, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.243827164
                            0.658950627
                            1
                        }
                        values: list[vec3] = {
                            { 1.01339281, 1.01339281, 1.01339281 }
                            { 0.53125, 0.53125, 0.53125 }
                            { 0.0803571418, 0.0803571418, 0.0803571418 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_flareblue.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "Avatar"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.330006868, 0.800000012, 1, 0.600000024 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.00129414455, 0.800000012, 1, 0.600000024 }
                            { 0.330006868, 0.800000012, 1, 0 }
                        }
                    }
                }
                pass: i16 = 19
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
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
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.505423009
                                    0.75921911
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.206363633
                                    0.49545455
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "flash"
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_12.dds"
                blendMode: u8 = 4
                pass: i16 = 1
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
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
                            { 90, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 100, 100 }
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
                            { 300, 100, 100 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_sparkMote.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "flash1"
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_12.dds"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0627451017, 0.529411793, 0.698039234, 1 }
                }
                meshRenderFlags: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0304761901
                                0.275377125
                                0.670278072
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.626332283
                                0.903448284
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
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
                            { 90, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.197231829
                            0.484429061
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 0.563636363, 0, 0 }
                            { 0.272727281, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Aura_Self.DDS"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "Avatar1"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.330006868, 0.800000012, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.00129414455, 0.800000012, 1, 0.500007629 }
                            { 0.330006868, 0.800000012, 1, 0 }
                        }
                    }
                }
                pass: i16 = 19
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Passive_Glow_A.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
            }
        }
        particleName: string = "Volibear_Skin03_Recall_ThunderClap_02"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_ThunderClap_02"
        flags: u16 = 197
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_ThunderClap_03" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 8
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                lifetime: option[f32] = {
                    8.5
                }
                emitterName: string = "Add1"
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
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.601482213
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.489997715 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 250, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.243827164
                            0.658950627
                            1
                        }
                        values: list[vec3] = {
                            { 1.01339281, 1.01339281, 1.01339281 }
                            { 0.53125, 0.53125, 0.53125 }
                            { 0.0803571418, 0.0803571418, 0.0803571418 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/common_flareblue.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "glowcracks"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0666666701, 0.909803927, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.0666666701, 0.909803927, 1, 1 }
                            { 0.0666666701, 0.909803927, 1, 0 }
                        }
                    }
                }
                pass: i16 = 19
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionFeatherIn: f32 = 0.200000003
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Passive_Glow_A.dds"
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.505423009
                                    0.75921911
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.100000001
                                    0.206363633
                                    0.49545455
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.300000012
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "flash"
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_12.dds"
                blendMode: u8 = 4
                pass: i16 = 1
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
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
                            { 90, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 100, 100 }
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
                            { 300, 100, 100 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_sparkMote.dds"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "flash1"
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_12.dds"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0627451017, 0.529411793, 0.698039234, 1 }
                }
                meshRenderFlags: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0304761901
                                0.275377125
                                0.670278072
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.626332283
                                0.903448284
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
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
                            { 90, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.197231829
                            0.484429061
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 0.563636363, 0, 0 }
                            { 0.272727281, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Aura_Self.DDS"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "flashbod"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.333333343, 0.800000012, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.00130718958, 0.800000012, 1, 1 }
                            { 0.333333343, 0.800000012, 1, 0 }
                        }
                    }
                }
                pass: i16 = 19
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.400000006, 0.200000003 }
                }
            }
        }
        particleName: string = "Volibear_Skin03_Recall_ThunderClap_03"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_ThunderClap_03"
        flags: u16 = 197
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_R_SpikeA" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_zeroStacks_R_SpikeA"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_R_SpikeA"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_R_SpikeB" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_zeroStacks_R_SpikeB"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_R_SpikeB"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_R_SpikeC" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_zeroStacks_R_SpikeC"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_R_SpikeC"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Q_aura" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "black"
                translationOverride: vec3 = { 0, -50, 0 }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 50 }
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
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_12.dds"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.164705887, 0.200000003, 0.384313732, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            -0.0103347898
                            0.765510678
                            0.983897924
                        }
                        values: list[vec4] = {
                            { 0.164705887, 0.200000003, 0.384313732, 1 }
                            { 0.164705887, 0.200000003, 0.384313732, 1 }
                            { 0.164705887, 0.200000003, 0.384313732, 0 }
                        }
                    }
                }
                pass: i16 = -1
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_ball32_02.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
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
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "flash"
                importance: u8 = 2
                translationOverride: vec3 = { 0, -100, 0 }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 50 }
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
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_02.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                pass: i16 = -1
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 200, 200 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.5, 0.5, 0.5 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Flash_01.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "avatarFlash"
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
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0496083535
                            0.122715406
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.470588237, 0.843137264, 1, 0.309803933 }
                            { 0, 0.0156862754, 1, 0.117647059 }
                            { 0.701960802, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_Glow_B.dds"
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 0 }
                    fresnel: f32 = 0.0299999993
                    fresnelColor: vec4 = { 0, 0.670588255, 0.956862748, 1 }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLinger: option[f32] = {
                    0.25
                }
                lifetime: option[f32] = {
                    4
                }
                emitterLinger: option[f32] = {
                    0.25
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 40 }
                }
                emitterName: string = "Trail_FlatBlend1"
                translationOverride: vec3 = { 0, -50, 0 }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 150 }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x2fec8a25: flag = true
                    0x6b77a8ca: embed = ValueColor {
                        constantValue: vec4 = { 0.121568628, 0.521568656, 0.717647076, 1 }
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.988913536
                            }
                            values: list[vec4] = {
                                { 0.121568628, 0.521568656, 0.717647076, 1 }
                                { 0.121568628, 0.521568656, 0.717647076, 0 }
                            }
                        }
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
                primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 800
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 300, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                        mMaxAddedPerFrame: i32 = 20
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0414343365
                            0.679662347
                            0.988913536
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.101960786, 0.431372553, 0.596078455, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0962939486
                            0.814372182
                            0.993348122
                        }
                        values: list[vec4] = {
                            { 0.101960786, 0.431372553, 0.596078455, 0 }
                            { 0.101960786, 0.431372553, 0.596078455, 1 }
                            { 0.101960786, 0.431372553, 0.596078455, 1 }
                            { 0.101960786, 0.431372553, 0.596078455, 0 }
                        }
                    }
                }
                pass: i16 = 99
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.00416666688
                                0.0340848826
                                0.0686587319
                                0.212852359
                                0.329558581
                                0.448607117
                                0.73809278
                                0.89187187
                                1
                            }
                            values: list[f32] = {
                                1
                                0.192660555
                                0
                                0
                                0.0964958817
                                0.251495808
                                0.771866262
                                0.938431442
                                1
                            }
                        }
                    }
                    0x26b4e623: bool = true
                    0x7d4f3ccc: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0785597414
                                0.22585924
                                1
                            }
                            values: list[f32] = {
                                0
                                0.489130437
                                0.782608688
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.449999988
                    erosionFeatherOut: f32 = 0.449999988
                    erosionMapName: string = "ASSETS/Characters/Senna/Skins/Base/Particles/Senna_Base_AutoAttack_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 200, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.159671038
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Senna/Skins/Base/Particles/Senna_Base_E_mistTrailSoft.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 4, 1 }
                emitterUvScrollRate: vec2 = { -2, 0 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.349999994
                }
                particleLinger: option[f32] = {
                    0.25
                }
                lifetime: option[f32] = {
                    4
                }
                emitterLinger: option[f32] = {
                    0.25
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 40 }
                }
                emitterName: string = "Trail_VertAdd2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 150 }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x2fec8a25: flag = true
                    0x6b77a8ca: embed = ValueColor {
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.988913536
                            }
                            values: list[vec4] = {
                                { 1, 1, 1, 1 }
                                { 1, 1, 1, 0 }
                            }
                        }
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
                primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 800
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 300, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                        mMaxAddedPerFrame: i32 = 20
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0414343365
                            0.679662347
                            0.988913536
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.501960814 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.498935759
                            0.993348122
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.501960814 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 102
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.00416666688
                                0.0264975801
                                0.0878875479
                                0.198781326
                                0.330637991
                                0.510748208
                                0.664527297
                                1
                            }
                            values: list[f32] = {
                                1
                                0
                                0
                                0.146145105
                                0.401985377
                                0.704639375
                                0.871204555
                                1
                            }
                        }
                    }
                    0x26b4e623: bool = true
                    0x7d4f3ccc: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0785597414
                                0.22585924
                                1
                            }
                            values: list[f32] = {
                                0
                                0.489130437
                                0.782608688
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.449999988
                    erosionFeatherOut: f32 = 0.449999988
                    erosionMapName: string = "ASSETS/Characters/Senna/Skins/Base/Particles/Senna_Base_AutoAttack_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 100, 100 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.833765745
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Senna/Skins/Base/Particles/Senna_Base_E_mistTrailSoft.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 4, 1 }
                emitterUvScrollRate: vec2 = { -3, 0 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    4
                }
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = 0xf8e30f62
                        }
                    }
                }
                emitterName: string = "Runes"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -50 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 2 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.107281551
                            0.257281542
                            0.91796118
                            1
                        }
                        values: list[f32] = {
                            1
                            0.443925232
                            0.189252332
                            0.0500000007
                            0.0500000007
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 40, 0, 0 }
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
                                { 40, 0, 0 }
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
                color: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0279069766
                            0.646511614
                            0.990697682
                        }
                        values: list[vec4] = {
                            { 0, 0, 0, 0 }
                            { 0, 0, 0, 1 }
                            { 0, 0, 0, 1 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.00416666688
                                0.212852359
                                0.329558581
                                0.448607117
                                0.73809278
                                0.89187187
                                1
                            }
                            values: list[f32] = {
                                0.0470085479
                                0
                                0.0964958817
                                0.251495808
                                0.771866262
                                0.938431442
                                1
                            }
                        }
                    }
                    0x26b4e623: bool = true
                    0x7d4f3ccc: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0785597414
                                0.22585924
                                1
                            }
                            values: list[f32] = {
                                0
                                0.489130437
                                0.782608688
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.150000006
                    erosionFeatherOut: f32 = 0.150000006
                    erosionMapName: string = "ASSETS/Characters/Senna/Skins/Base/Particles/Senna_Base_AutoAttack_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 10, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    0.25
                }
                lifetime: option[f32] = {
                    5
                }
                emitterLinger: option[f32] = {
                    0.25
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 40 }
                }
                emitterName: string = "Trail_Blendo"
                translationOverride: vec3 = { 0, -50, 0 }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 150 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x2fec8a25: flag = true
                    0x6b77a8ca: embed = ValueColor {
                        constantValue: vec4 = { 0.121568628, 0.521568656, 0.717647076, 1 }
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.988913536
                            }
                            values: list[vec4] = {
                                { 0.121568628, 0.521568656, 0.717647076, 1 }
                                { 0.121568628, 0.521568656, 0.717647076, 0 }
                            }
                        }
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
                primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 1200
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                        mMaxAddedPerFrame: i32 = 20
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0414343365
                            0.679662347
                            0.988913536
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.100007631, 0.429999232, 0.600000024, 0.400000006 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.187461659
                            0.548466384
                            0.993348122
                        }
                        values: list[vec4] = {
                            { 0.100007631, 0.429999232, 0.600000024, 0 }
                            { 0.100007631, 0.429999232, 0.599999964, 0.400000006 }
                            { 0.100007631, 0.429999232, 0.600000024, 0.400000006 }
                            { 0.100007631, 0.429999232, 0.600000024, 0 }
                        }
                    }
                }
                pass: i16 = 98
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.00416666688
                                0.0340848826
                                0.0686587319
                                0.212852359
                                0.329558581
                                0.448607117
                                0.73809278
                                0.89187187
                                1
                            }
                            values: list[f32] = {
                                1
                                0.192660555
                                0
                                0
                                0.0964958817
                                0.251495808
                                0.771866262
                                0.938431442
                                1
                            }
                        }
                    }
                    0x26b4e623: bool = true
                    0x7d4f3ccc: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.163817286
                                0.227353469
                                0.444331706
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.485074639
                                0.931862414
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.600000024
                    erosionFeatherOut: f32 = 0.600000024
                    erosionMapName: string = "ASSETS/Characters/Senna/Skins/Base/Particles/Senna_Base_AutoAttack_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 160, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.159671038
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Q_RuneTrail_A.dds"
                emitterUvScrollRate: vec2 = { -0.5, 0 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLinger: option[f32] = {
                    0.25
                }
                lifetime: option[f32] = {
                    5
                }
                emitterLinger: option[f32] = {
                    0.25
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 0.100000001, 40 }
                }
                emitterName: string = "Trail_Add"
                translationOverride: vec3 = { 0, -50, 0 }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 150 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                0xb929b43e: pointer = 0x9b19f2b5 {
                    0x2fec8a25: flag = true
                    0x6b77a8ca: embed = ValueColor {
                        dynamics: pointer = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.988913536
                            }
                            values: list[vec4] = {
                                { 1, 1, 1, 1 }
                                { 1, 1, 1, 0 }
                            }
                        }
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
                primitive: pointer = VfxPrimitiveArbitraryTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 1200
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                        mMaxAddedPerFrame: i32 = 20
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0414343365
                            0.679662347
                            0.988913536
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.119657613
                            0.291924655
                            0.451600701
                            0.993348122
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.800000012 }
                            { 0.400000006, 0.890196085, 1, 0.800000012 }
                            { 0.0196078438, 0.607843161, 1, 0 }
                        }
                    }
                }
                pass: i16 = 99
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.00416666688
                                0.0340848826
                                0.0686587319
                                0.212852359
                                0.329558581
                                0.448607117
                                0.73809278
                                0.89187187
                                1
                            }
                            values: list[f32] = {
                                1
                                0.192660555
                                0
                                0
                                0.0964958817
                                0.251495808
                                0.771866262
                                0.938431442
                                1
                            }
                        }
                    }
                    0x26b4e623: bool = true
                    0x7d4f3ccc: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.163817286
                                0.227353469
                                0.444331706
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.485074639
                                0.931862414
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.600000024
                    erosionFeatherOut: f32 = 0.600000024
                    erosionMapName: string = "ASSETS/Characters/Senna/Skins/Base/Particles/Senna_Base_AutoAttack_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 0, 1, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 160, 80, 80 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.159671038
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                            { 0.800000012, 0.800000012, 0.800000012 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Q_RuneTrail_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                emitterUvScrollRate: vec2 = { -0.5, 0 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "RuneAddHead"
                translationOverride: vec3 = { 0, -50, 0 }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 80, -40 }
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
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_12.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.250980407, 0.764705896, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            -0.0103347898
                            0.835236073
                            0.983897924
                        }
                        values: list[vec4] = {
                            { 0.250980407, 0.764705896, 1, 1 }
                            { 0.250980407, 0.764705896, 1, 1 }
                            { 0.250980407, 0.764705896, 1, 0 }
                        }
                    }
                }
                pass: i16 = 2
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Runes_02.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                numFrames: u16 = 4
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Ashe_Skin03_ground_CrackNoise_mult.dds"
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
                    constantValue: f32 = 5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "RuneoBodBlend"
                translationOverride: vec3 = { 0, -50, 0 }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 140, 100 }
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
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_12.dds"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.450003803, 0.960006118, 1, 0.300007641 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            -0.0103347898
                            0.858163893
                            0.983897924
                        }
                        values: list[vec4] = {
                            { 0.450003803, 0.960006118, 1, 0.300007641 }
                            { 0.450003803, 0.960006118, 1, 0.300007641 }
                            { 0.450003803, 0.960006118, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 85, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 60, 1 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Runes_02.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                numFrames: u16 = 4
                startFrame: u16 = 2
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "RuneoBlendHead"
                translationOverride: vec3 = { 0, -50, 0 }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 80, -40 }
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
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_12.dds"
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.250003815, 0.76000613, 1, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            -0.0103347898
                            0.860068262
                            1
                        }
                        values: list[vec4] = {
                            { 0.250003815, 0.76000613, 1, 0.500007629 }
                            { 0.250003815, 0.76000613, 1, 0.500007629 }
                            { 0.250003815, 0.76000613, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Runes_02.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "RuneoBodAdd"
                translationOverride: vec3 = { 0, -50, 0 }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 140, 100 }
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
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_12.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.250980407, 0.764705896, 1, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            -0.0103347898
                            0.835236073
                            0.983897924
                        }
                        values: list[vec4] = {
                            { 0.250980407, 0.764705896, 1, 0.800000012 }
                            { 0.250980407, 0.764705896, 1, 0.800000012 }
                            { 0.250980407, 0.764705896, 1, 0 }
                        }
                    }
                }
                pass: i16 = 2
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 85, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 60, 1 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Runes_02.dds"
                birthFrameRate: embed = ValueFloat {
                    constantValue: f32 = 0
                }
                numFrames: u16 = 4
                startFrame: u16 = 2
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Ashe_Skin03_ground_CrackNoise_mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1 }
                    }
                }
            }
        }
        particleName: string = "Volibear_Skin03_Q_aura"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Q_aura"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_L_SpikeB" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_zeroStacks_L_SpikeB"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_L_SpikeB"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_L_SpikeC" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_zeroStacks_L_SpikeC"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_L_SpikeC"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_L_SpikeA" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_zeroStacks_L_SpikeA"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_L_SpikeA"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_R_SpikeB" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_maxStacks_R_SpikeB"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_R_SpikeB"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_R_SpikeC" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_maxStacks_R_SpikeC"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_R_SpikeC"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_R_SpikeA" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_maxStacks_R_SpikeA"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_R_SpikeA"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Q_cast" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
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
                    0.25
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh2"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 10 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Q_Swipe_A.scb"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0980392173, 0.200000003, 0.223529413, 0.800000012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0681293309
                            1
                        }
                        values: list[vec4] = {
                            { 0.0980392173, 0.200000003, 0.223529413, 0 }
                            { 0.0980392173, 0.200000003, 0.223529413, 0.800000012 }
                            { 0.0980392173, 0.200000003, 0.223529413, 0 }
                        }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Q_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -1.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -1.5 }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    0.699999988
                }
                lifetime: option[f32] = {
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh7"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 10 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Q_Swipe_A.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0681293309
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 5
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
                    erosionFeatherIn: f32 = 0.600000024
                    erosionFeatherOut: f32 = 0.600000024
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_RuneSwipe.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 1.5 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.175086483
                            0.322851151
                            0.557651997
                            0.702306092
                            1
                        }
                        values: list[vec2] = {
                            { 0, 1.5 }
                            { 0, 1.5 }
                            { 0, 1.24361742 }
                            { 0, 0.584070802 }
                            { 0, 0.292035401 }
                            { 0, 0 }
                        }
                    }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Q_Swipe_A.dds"
                    texAddressModeMult: u8 = 2
                    0x22c3cf3e: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, -2 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                0.175086483
                                0.322851151
                                0.557651997
                                0.702306092
                                1
                            }
                            values: list[vec2] = {
                                { 0, -2 }
                                { 0, -2 }
                                { 0, -1.65815663 }
                                { 0, -0.778761089 }
                                { 0, -0.389380544 }
                                { 0, -0 }
                            }
                        }
                    }
                    birthUVOffsetMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 1.10000002 }
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
                    0.5
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh8"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 10 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Q_Swipe_A.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0681293309
                            0.279816508
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
                pass: i16 = 4
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_BasicAttack_swipe_B.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, -0.100000001 }
                }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2 }
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
                    0.25
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_Mesh9"
                0x3bf0b4ed: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 10 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Q_Swipe_A.scb"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.590005338, 0.800000012, 0.940001547, 0.500007629 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0681293309
                            1
                        }
                        values: list[vec4] = {
                            { 0.590005338, 0.800000012, 0.940001547, 0 }
                            { 0.590005338, 0.800000012, 0.940001547, 0.500007629 }
                            { 0.590005338, 0.800000012, 0.940001547, 0 }
                        }
                    }
                }
                pass: i16 = 4
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Q_Swipe_A.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                }
                texAddressModeBase: u8 = 2
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, -2 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, -2 }
                        }
                    }
                }
            }
        }
        particleName: string = "Volibear_Skin03_Q_cast"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Q_cast"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_Aura_01" = VfxSystemDefinitionData {
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
                emitterName: string = "Avatar1"
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
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.847058833, 0.921568632, 1, 0.501960814 }
                }
                pass: i16 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionFeatherIn: f32 = 0.5
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Passive_Glow_A.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 0 }
                    fresnel: f32 = 0.100000001
                    fresnelColor: vec4 = { 0.0196078438, 0.313725501, 0.670588255, 1 }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_impactErode.dds"
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
        }
        particleName: string = "Volibear_Skin03_Passive_zeroStacks_Aura_01"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_Aura_01"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_L_SpikeA" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_midStacks_L_SpikeA"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_L_SpikeA"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_L_SpikeB" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_midStacks_L_SpikeB"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_L_SpikeB"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_L_SpikeC" = VfxSystemDefinitionData {
        particleName: string = "Volibear_Skin03_Passive_midStacks_L_SpikeC"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_L_SpikeC"
    }
    "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 11
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "bodyAdd_A"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0151051581
                            0.955795765
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
                pass: i16 = 2
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Passive_Glow_A.dds"
                }
                depthBiasFactors: vec2 = { -1, -4 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Ashe_Base_ground_CrackNoise_mult.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.100000001, 0.100000001 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 11
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "bodyBlend"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.105882354, 0.294117659, 0.349019617, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0151051581
                            0.955795765
                            1
                        }
                        values: list[vec4] = {
                            { 0.105882354, 0.294117659, 0.349019617, 0 }
                            { 0.105882354, 0.294117659, 0.349019617, 1 }
                            { 0.105882354, 0.294117659, 0.349019617, 1 }
                            { 0.105882354, 0.294117659, 0.349019617, 0 }
                        }
                    }
                }
                pass: i16 = 1
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin03/Particles/Volibear_Skin03_Passive_Glow_A.dds"
                }
                depthBiasFactors: vec2 = { -1, -4 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteCount: i32 = 16
                }
            }
        }
        particleName: string = "Volibear_Skin03_Recall_01"
        particlePath: string = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_01"
        flags: u16 = 198
    }
    0x113e43a6 = GearSkinUpgrade {
        mGearData: pointer = GearData {
            mVFXResourceResolver: pointer = ResourceResolver {}
        }
    }
    0x70c00708 = GearSkinUpgrade {
        mGearData: pointer = GearData {
            mVFXResourceResolver: pointer = ResourceResolver {}
        }
    }
    0xf74bc37b = GearSkinUpgrade {
        mGearData: pointer = GearData {
            mVFXResourceResolver: pointer = ResourceResolver {}
        }
    }
    0xfc04cb75 = GearSkinUpgrade {
        mGearData: pointer = GearData {
            mVFXResourceResolver: pointer = ResourceResolver {}
        }
    }
    "Characters/Volibear/Skins/Skin3/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Volibear_R_attack_buf_L" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_R_attack_buf_L"
            "Volibear_R_attack_buf_R" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_R_attack_buf_R"
            0x9302b6d3 = 0x6dea0f58
            0xbabd2161 = 0xe24cb79e
            0xdeb570a5 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_R_Buf_Max"
            0x339465c4 = 0x3f47ddf7
            0x5d587cca = 0xd0f73971
            0x3426454d = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_Aura_01"
            0x86cad419 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Q_cast"
            0x255cc173 = 0xd976c74e
            0xeeb9b013 = 0x5c9f5368
            0x430a78d7 = 0x0de16d06
            0xefccc0de = 0x0de16d06
            0x26e4bfc3 = 0x273787e6
            0x19a7d548 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_BasicAttack_Swipe_R_01"
            0x5175695e = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_BasicAttack_Swipe_L_01"
            0x79ea8ec0 = 0xcb5f78a9
            0xca178bf5 = 0x242f98ca
            0x2076dd33 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_E_AOE"
            0xcfe5ced8 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_E_AOE_Warning"
            0x34a4196b = 0x0f36fb08
            0x7e2af041 = 0x2c6094d6
            0x4c352fd2 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_L_SpikeA"
            0x4b352e3f = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_L_SpikeB"
            0x4a352cac = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_L_SpikeC"
            0xe36387f0 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_R_SpikeA"
            0xe6638ca9 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_R_SpikeB"
            0xe5638b16 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_R_SpikeC"
            0xcfdc69a6 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_L_SpikeA"
            0xcedc6813 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_L_SpikeB"
            0xcddc6680 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_L_SpikeC"
            0x01ab2a3c = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_R_SpikeA"
            0x04ab2ef5 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_R_SpikeB"
            0x03ab2d62 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_maxStacks_R_SpikeC"
            0x95bf28e2 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_L_SpikeA"
            0x94bf274f = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_L_SpikeB"
            0x93bf25bc = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_L_SpikeC"
            0x2e517920 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_R_SpikeA"
            0x31517dd9 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_R_SpikeB"
            0x30517c46 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_R_SpikeC"
            0x178c0831 = 0xfd7ce94e
            0x04fe08a9 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_midStacks_Aura_01"
            0x04719679 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Passive_zeroStacks_Aura_01"
            0x2cd330c5 = 0xc2e77732
            0xd6565e3e = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_W_Marked"
            0x46d2dfd3 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Q_aura"
            0x6d78ac72 = 0x01b543d4
            0xd2c8fa6f = 0x6bf5276c
            0xbe6a7615 = 0xdb467fc7
            0x9852d67e = 0x8a1a93d3
            0x4543e999 = 0x83d9bf05
            0xead3c256 = 0x74978bae
            0xacf17fa8 = 0x95d9db5b
            0x338f637d = 0x57b754e2
            0xb9c9d361 = 0x1d1519e0
            0x243e81b6 = 0x80ff550f
            0xac47b4f2 = 0xe49dbc07
            0xc65b4dee = 0x6dbdaa75
            0x4a8e6c32 = 0x16cff8eb
            0x19f2b094 = 0xa603ad29
            0xd68d8ea4 = 0xc0376651
            0x3190c9e3 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_W_Slash"
            0xb64e604f = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_W_Marked_Scratch"
            0x34aeb891 = 0xe69ee834
            0x631db25c = 0xfc426561
            0x173ad995 = 0xf94260a8
            0x8aa39859 = 0xf7783e08
            0xf26df310 = 0x56c9ec3d
            0x54310ad9 = 0x2cd288c6
            0xdd587971 = 0x1d040de6
            0xf475415d = 0x87a4fc6c
            0xf7bec269 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_01"
            0x1877a055 = 0xe88e5370
            0x9291ddb9 = 0xf1012f1a
            0xed60495a = 0x5a8dc989
            0xf39d67a6 = 0x0202ef69
            0x772825b8 = 0x88bc34a9
            0x1571890e = 0x3e65c86d
            0xf7c7b804 = 0xbcfaf072
            0x7cedf3f7 = 0x68d1f77c
            0x14b4d573 = 0x0a179cc6
            0xbeba5d20 = 0x724af32f
            0xc8cfc575 = 0xd649ba80
            0xbd1b28fe = 0xfcf7707f
            0xdaebc7e8 = 0x74eec27d
            0x59e92b92 = 0x91c59ec5
            0xc66563b6 = 0xe3911b53
            0x69331747 = 0x5d549f5c
            0xf8e30f62 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Q_floatyRunes"
            0x09ea8bc3 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_Rock_A"
            0x0aea8d56 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_Rock_B"
            0x0bea8ee9 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_Rock_C"
            0xaa0c026c = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_ThunderClap_01"
            0xad0c0725 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_ThunderClap_02"
            0xac0c0592 = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Skin03_Recall_ThunderClap_03"
        }
    }
}
