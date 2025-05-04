#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Volibear_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin7_Skins_Skin9.bin"
    "DATA/Volibear_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin9.bin"
    "DATA/Characters/Volibear/Volibear.bin"
    "DATA/Characters/Volibear/Animations/Skin0.bin"
    "DATA/Volibear_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin7.bin"
    "DATA/Volibear_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin9.bin"
    "DATA/Volibear_Skins_Skin0_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin7_Skins_Skin9.bin"
    "DATA/Volibear_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin7_Skins_Skin9.bin"
}
entries: map[hash,embed] = {
    "Characters/Volibear/Skins/Skin16" = SkinCharacterDataProperties {
        skinClassification: u32 = 2
        championSkinName: string = "VolibearSkin16"
        skinParent: i32 = 7
        metaDataTags: string = "faction:freljord,gender:male,element:lightning,race:demigod,skinline:dragonmancers"
        skinUpgradeData: embed = skinUpgradeData {
            mGearSkinUpgrades: list[link] = {
                0x3ed9d29c
                0xdde70b17
                0x6c1939aa
                0x06b613c1
            }
        }
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Characters/Volibear/Skins/Skin07/VolibearLoadscreen_7.tex"
        }
        loadscreenVintage: embed = CensoredImage {
            image: string = "ASSETS/Characters/Volibear/Skins/Skin07/VolibearLoadscreen_7_LE.tex"
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
    "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_R_Buf_Max" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.600000024
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 11.8500004
                }
                particleLinger: option[f32] = {
                    0.150000006
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
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.596078455, 0.596078455, 0.890196085, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.00900361873
                            0.924242377
                            0.955334961
                            0.981518269
                            1
                        }
                        values: list[vec4] = {
                            { 0.596078455, 0.596078455, 0.890196085, 0 }
                            { 0.596078455, 0.596078455, 0.890196085, 0.250003815 }
                            { 0.596078455, 0.596078455, 0.890196085, 1 }
                            { 0.184667438, 0.187004998, 0.429388702, 0.963855445 }
                            { 0.147266433, 0.156616688, 0.28276819, 0.850980401 }
                            { 0.0647758245, 0.0717885122, 0.149102062, 0 }
                        }
                    }
                }
                meshRenderFlags: u8 = 0
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { 1, 4 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Ult_Clouds_A.dds"
                uvMode: u8 = 1
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.0500000007 }
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
                emitterName: string = "EndFlash"
                Linger: pointer = VfxLingerDefinitionData {
                    UseLingerScale: flag = true
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
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
                EmitterPosition: embed = ValueVector3 {
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
                            "Mane"
                        }
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
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 0, 0 }
                    }
                    paletteCount: i32 = 16
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
                    0.150000006
                }
                lifetime: option[f32] = {
                    2
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "Stencil_Mask"
                Linger: pointer = VfxLingerDefinitionData {
                    UseLingerScale: flag = true
                    LingerScale: embed = ValueVector3 {
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
                    UseSeparateLingerColor: flag = true
                    SeparateLingerColor: embed = ValueColor {
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
                        mSubmeshesToDraw: list[hash] = {
                            "Mane"
                            "BODY"
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
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Dissolve_Cloudy_01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                stencilMode: u8 = 1
                stencilRef: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
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
                emitterName: string = "bodyBlend_A"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                            "Mane"
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            "UltGear"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.899999976
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
                pass: i16 = -1
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_AvatarTexture_UltBase.dds"
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
                emitterName: string = "bodyFresnel_A"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                            "Mane"
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
                            { 0, 0, 0, 0.963855445 }
                            { 0, 0, 0, 0.850980401 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = -1.10000002
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_R_Avatar_Blend_01.dds"
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 0 }
                    fresnel: f32 = 0.0299999993
                    fresnelColor: vec4 = { 0.596078455, 0.596078455, 0.890196085, 1 }
                }
                depthBiasFactors: vec2 = { -1, -3 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 1.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.800000012
                }
                lifetime: option[f32] = {
                    12
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
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 20, 350, 30 }
                }
                EmitterPosition: embed = ValueVector3 {
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.192156866, 0.192156866, 0.286274523, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.102908276
                            0.304250568
                            0.455700666
                            1
                        }
                        values: list[vec4] = {
                            { 0.192156866, 0.192156866, 0.286274523, 0 }
                            { 0.192156866, 0.192156866, 0.286274523, 0.156626508 }
                            { 0.192156866, 0.192156866, 0.286274523, 0.759464204 }
                            { 0.192156866, 0.192156866, 0.286274523, 1 }
                            { 0.192156866, 0.192156866, 0.286274523, 1 }
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
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Cas_Dust_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
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
                emitterName: string = "Avatar"
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
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
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
                            { 0.192156866, 0.192156866, 0.286274523, 1 }
                            { 0.596078455, 0.596078455, 0.890196085, 1 }
                            { 0.160006106, 0.149996191, 0.250003815, 1 }
                            { 1, 1, 1, 0 }
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
                timeBeforeFirstEmission: f32 = 0.649999976
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "AV_ChromaticAbberation_B"
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
                SpawnShape: pointer = VfxShapeSphere {
                    flags: u8 = 1
                    radius: f32 = 5
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
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
                    constantValue: vec4 = { 1, 1, 1, 0.250003815 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.737254918, 0.741176486, 0.890196085, 0 }
                            { 0.192156866, 0.192156866, 0.286274523, 1 }
                            { 0.156862751, 0.149019614, 0.250980407, 0 }
                        }
                    }
                }
                pass: i16 = 9999
                meshRenderFlags: u8 = 0
                depthBiasFactors: vec2 = { -1, -120 }
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
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Draven_Base_W_Color-hold.DDS"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.75
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
                }
                particleLinger: option[f32] = {
                    0.150000006
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar1"
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
                    constantValue: vec4 = { 0, 0, 0, 0.501960814 }
                }
                pass: i16 = 20
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -120 }
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
                    constantValue: f32 = 25
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
                                    0.699999988
                                    1.29999995
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
                    0.150000006
                }
                lifetime: option[f32] = {
                    10
                }
                isSingleParticle: flag = true
                emitterName: string = "Main_Shape_Clouds"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.200000003, 0 }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1700, 200, 100 }
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 1700, 200, 100 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 12, 2, 12 }
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
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 50
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 15, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.400000006 }
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.400000006 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.396078438, 0.396078438, 0.396078438, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.204167753
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.233688399, 0.340626836, 0.372314334, 0 }
                            { 0.17427209, 0.178236797, 0.281216592, 0.500007629 }
                            { 0.175517112, 0.175517112, 0.372779697, 1 }
                            { 0.108727418, 0.121153407, 0.166197628, 0.101960786 }
                            { 0.0434909649, 0.0357247218, 0.0683429465, 0 }
                        }
                    }
                }
                pass: i16 = 20
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 3
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.119031653
                                0.641751826
                                1
                            }
                            values: list[f32] = {
                                -0.0481283404
                                -0.0802139044
                                0.966279805
                                3
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/LeeSin_Skin31_E_clouds_erosion_2.dds"
                }
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
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
                            VfxProbabilityTableData {}
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -15, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 125, 230, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 125, 230, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.549101591
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.953711808, 0.800000012, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/LeeSin_Skin31_E_clouds.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Mist.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
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
                    constantValue: f32 = 25
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
                                    0.850000024
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
                    0.150000006
                }
                lifetime: option[f32] = {
                    12
                }
                emitterName: string = "SmolFlames"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 350, 300 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.850000024
                                    1.25
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 350, 300 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 75
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.160006106, 0.149996191, 0.250003815, 0 }
                            { 0.156862751, 0.149019614, 0.250980407, 1 }
                            { 0.0800030529, 0.0800030529, 0.140001521, 0 }
                        }
                    }
                }
                pass: i16 = 40
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0
                                0.200000003
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_FlameFB_4x2_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -180 }
                stencilMode: u8 = 2
                stencilRef: u8 = 2
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 45, 0 }
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
                            { 360, 45, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 75, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
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
                            { 100, 75, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_FlameFB_4x2.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 3, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 2 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.800000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                lifetime: option[f32] = {
                    12
                }
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "Stencil_Mask1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 300 }
                }
                Linger: pointer = VfxLingerDefinitionData {
                    UseLingerScale: flag = true
                    LingerScale: embed = ValueVector3 {
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
                    UseSeparateLingerColor: flag = true
                    SeparateLingerColor: embed = ValueColor {
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
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 30 }
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "Mane"
                            "BODY"
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            "UltGear"
                        }
                    }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
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
                pass: i16 = -1
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
                    erosionFeatherIn: f32 = 0.300000012
                    erosionFeatherOut: f32 = 0.300000012
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Dissolve_Cloudy_01.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { 1, 80 }
                miscRenderFlags: u8 = 1
                stencilMode: u8 = 1
                stencilRef: u8 = 2
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 12
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "WhiteOutline"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -10, 0 }
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
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.899999976
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
                pass: i16 = -300
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { 1, 50 }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1.04999995, 1.01999998 }
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
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.192156866, 0.192156866, 0.286274523, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.159268931
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.192156866, 0.192156866, 0.286274523, 0 }
                            { 0.192156866, 0.192156866, 0.286274523, 1 }
                            { 0.192156866, 0.192156866, 0.286274523, 1 }
                            { 0.192156866, 0.192156866, 0.286274523, 0 }
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
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Riven_Skin23_Z_Glow.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    0.150000006
                }
                lifetime: option[f32] = {
                    12
                }
                emitterName: string = "bodyBlend_A4"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "BODY"
                            "Mane"
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            "UltGear"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.596078455, 0.596078455, 0.890196085, 1 }
                            { 0.596078455, 0.596078455, 0.890196085, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 600
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -25 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_AvatarTexture_Passive_Glow.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.649999976
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                lifetime: option[f32] = {
                    12
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
                SpawnShape: pointer = VfxShapeSphere {
                    flags: u8 = 1
                    radius: f32 = 5
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
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
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.737254918, 0.741176486, 0.890196085, 0 }
                            { 0.192156866, 0.192156866, 0.286274523, 1 }
                            { 0.156862751, 0.149019614, 0.250980407, 0 }
                        }
                    }
                }
                meshRenderFlags: u8 = 0
                depthBiasFactors: vec2 = { 1, 180 }
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
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Draven_Base_W_Color-hold.DDS"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
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
                                    0.850000024
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
                    12
                }
                emitterName: string = "SmolFlames2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 25, 300 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.850000024
                                    1.25
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 25, 300 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 120, 0, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 250, 0 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 0.160006106, 0.149996191, 0.250003815, 0 }
                            { 0.596078455, 0.596078455, 0.890196085, 1 }
                            { 0.0800030529, 0.0800030529, 0.140001521, 0 }
                        }
                    }
                }
                pass: i16 = 40
                colorLookUpTypeY: u8 = 3
                depthBiasFactors: vec2 = { 1, 85 }
                stencilMode: u8 = 2
                stencilRef: u8 = 2
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 45, 0 }
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
                            { 360, 45, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 75, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
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
                            { 25, 75, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Cas_Dust_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 2 }
                    }
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
                    0.150000006
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "bodyBlend_A5"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "dragon"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.899999976
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
                pass: i16 = -1
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin16/Volibear_Skin16_Recall_TX_CM.dds"
            }
        }
        particleName: string = "Volibear_Skin16_R_Buf_Max"
        particlePath: string = "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_R_Buf_Max"
    }
    "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Emote_PoroJokeLoop" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.43300009
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "bodyBlend_A"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "PORO"
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            "PORO"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                pass: i16 = 40
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -6 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin16/Volibear_Skin16_Poro_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 160
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                particleLinger: option[f32] = {
                    0.400000006
                }
                lifetime: option[f32] = {
                    2
                }
                emitterName: string = "Temp_Trail"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 600, 0 }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 450, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.890196085, 0.890196085, 0.890196085, 0 }
                            { 0.466666669, 0.466666669, 0.698039234, 1 }
                            { 0.313725501, 0.541176498, 1, 0.729411781 }
                            { 0.176470593, 0.176470593, 0.266666681, 0.43921569 }
                            { 0, 0, 0.200000003, 0.140001521 }
                        }
                    }
                }
                pass: i16 = 10
                alphaRef: u8 = 0
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Samira_Base_R_Smoke_Trail.dds"
                texDiv: vec2 = { 0.5, 1 }
                emitterUvScrollRate: vec2 = { -0.5, 0 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    0.400000006
                }
                emitterName: string = "Temp_Trail1"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 450, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.980392158, 0.980392158, 0.980392158, 0 }
                            { 0.313725501, 0.541176498, 1, 1 }
                            { 0.333333343, 0.333333343, 0.498039216, 0.729411781 }
                            { 0.176470593, 0.176470593, 0.266666681, 0.43921569 }
                            { 0, 0, 0.200000003, 0.140001521 }
                        }
                    }
                }
                pass: i16 = 9
                alphaRef: u8 = 0
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Kassadin_Skin14_Q_WispTrail_Add.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                }
                texDiv: vec2 = { 2, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.29999995
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
                    0.200000003
                }
                emitterName: string = "Main_Shape_Clouds"
                disabled: bool = true
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.200000003, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 2, 6 }
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeSphere {
                    flags: u8 = 1
                }
                EmitterPosition: embed = ValueVector3 {
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
                                    0.800000012
                                    1
                                }
                            }
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
                    constantValue: vec4 = { 0.396078438, 0.396078438, 0.396078438, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.204167753
                            0.546286941
                            0.747704744
                            1
                        }
                        values: list[vec4] = {
                            { 0.233688399, 0.340626836, 0.372314334, 0 }
                            { 0.17427209, 0.178236812, 0.281216592, 0.500007629 }
                            { 0.175517112, 0.175517112, 0.372779697, 1 }
                            { 0.108727418, 0.121153407, 0.166197628, 0.101960786 }
                            { 0.0434909649, 0.0357247218, 0.0683429465, 0 }
                        }
                    }
                }
                pass: i16 = 20
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 3
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.119031653
                                0.641751826
                                1
                            }
                            values: list[f32] = {
                                -0.0481283404
                                -0.0802139044
                                0.966279805
                                3
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/LeeSin_Skin31_E_clouds_erosion_2.dds"
                }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
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
                            VfxProbabilityTableData {}
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -15, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 125, 230, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 125, 230, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.549101591
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1, 0.800000012, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/LeeSin_Skin31_E_clouds.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Mist.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
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
                timeBeforeFirstEmission: f32 = 0.349999994
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
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
                                    0.200000003
                                    1.5
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
                    1.5
                }
                emitterName: string = "Embers"
                disabled: bool = true
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.5, 0 }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 300, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 1, 5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.25
                                }
                            }
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
                SpawnShape: pointer = VfxShapeSphere {
                    radius: f32 = 25
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 25 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.333333343, 0.333333343, 0.498039216, 0 }
                            { 0.474509805, 0.474509805, 0.564705908, 0.501960814 }
                            { 0.330006868, 0.330006868, 0.500007629, 1 }
                            { 0.141176477, 0.141176477, 0.211764708, 1 }
                            { 0.0627451017, 0.0627451017, 0.0941176489, 0 }
                        }
                    }
                }
                pass: i16 = 30
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
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
                    constantValue: vec3 = { 300, 0, 0 }
                }
                directionVelocityScale: f32 = 0.00300000003
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 60, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 60, 60, 50 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.129999995
                            0.400000006
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.20000005, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 0.5, 1 }
                            { 1, 0.5, 1 }
                            { 0, 0, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Brand_Skin08_Q_StardustMoteAlpha.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
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
                            1.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.699999988
                }
                emitterName: string = "SmallStarTrail"
                disabled: bool = true
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -0.5, 0 }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 50, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 1, 5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.25
                                }
                            }
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
                SpawnShape: pointer = VfxShapeSphere {
                    radius: f32 = 25
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 25 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.596078455, 0.596078455, 0.890196085, 1 }
                            { 0.333333343, 0.333333343, 0.498039216, 1 }
                            { 0.160784319, 0.160784319, 0.239215687, 1 }
                        }
                    }
                }
                pass: i16 = 85
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 90 }
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
                            { 1, 0, 90 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 0, 0 }
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
                            { 60, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 1, 1 }
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
                            { 20, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/EnergyMote.dds"
            }
        }
        particleName: string = "Volibear_Skin16_Emote_PoroJokeLoop"
        particlePath: string = "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Emote_PoroJokeLoop"
        flags: u16 = 197
    }
    "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_W_Chomp" = VfxSystemDefinitionData {
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
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "bearHeadAdd"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 200 }
                }
                Linger: pointer = VfxLingerDefinitionData {
                    KeyedLingerAcceleration: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, 2000 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin7_Spell2.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin7_Spell2.skl"
                        mAnimationName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Spell2.anm"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0743801668
                            0.833333313
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
                pass: i16 = 61
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.227722779
                                0.443069309
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.117647059
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { 1, 1 }
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
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
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Volibear_Skin07_TX_CM.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteCount: i32 = 16
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Wisp_Mult.dds"
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
                emitterName: string = "bearHeadBlend"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 200 }
                }
                Linger: pointer = VfxLingerDefinitionData {
                    KeyedLingerAcceleration: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, 2000 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin7_Spell2.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin7_Spell2.skl"
                        mAnimationName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Spell2.anm"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.669993162, 0.669993162, 1, 1 }
                }
                color: embed = ValueColor {
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
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.867318451 }
                            { 1, 1, 1, 0.23031646 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 60
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
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0, 0, 0, 0 }
                    fresnel: f32 = 0.00100000005
                    fresnelColor: vec4 = { 0.596078455, 0.596078455, 0.890196085, 1 }
                }
                depthBiasFactors: vec2 = { 1, 4 }
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
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
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin16/Volibear_Skin16_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.25
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[f32] = {
                            10
                            3
                        }
                    }
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
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                fieldCollectionDefinition: pointer = VfxFieldCollectionDefinitionData {
                    fieldAttractionDefinitions: list[embed] = {
                        VfxFieldAttractionDefinitionData {
                            position: embed = ValueVector3 {
                                constantValue: vec3 = { 0, 0, 100 }
                            }
                            radius: embed = ValueFloat {
                                constantValue: f32 = 3200
                            }
                            acceleration: embed = ValueFloat {
                                constantValue: f32 = 1600
                            }
                        }
                    }
                }
                emitterName: string = "guts_"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 100, -400 }
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
                                        0.800000012
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 50, 100, -400 }
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
                EmitterPosition: embed = ValueVector3 {
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
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_color-meatrot32_05.dds"
                pass: i16 = 10
                meshRenderFlags: u8 = 0
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 50
                censorModulateValue: vec4 = { 0, 0, 0, 1 }
                isUniformScale: flag = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 24, 24, 24 }
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
                            { 24, 24, 24 }
                        }
                    }
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
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 5, 5, 5 }
                            { 10, 10, 10 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_meatrot32_06.dds"
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
                disabled: bool = true
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 300 }
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 120, -400 }
                }
                EmitterPosition: embed = ValueVector3 {
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
                pass: i16 = 59
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
                    paletteCount: i32 = 16
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
                emitterName: string = "flash1"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 300 }
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 150, -300 }
                }
                EmitterPosition: embed = ValueVector3 {
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
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.152941182, 0.219607845, 0.262745112, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.0136363637
                            0.521029949
                            1
                        }
                        values: list[vec4] = {
                            { 0.152941182, 0.219607845, 0.262745112, 1 }
                            { 0.052000232, 0.112000503, 0.262745112, 0.280003041 }
                            { 0.0107048322, 0.0636857748, 0.262745112, 0 }
                        }
                    }
                }
                pass: i16 = 58
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
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Aura_Self.DDS"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
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
                    0.400000006
                }
                lifetime: option[f32] = {
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "TeethAdd"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 200 }
                }
                Linger: pointer = VfxLingerDefinitionData {
                    KeyedLingerAcceleration: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 0, 2000 }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Spell2.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Spell2.skl"
                        mAnimationName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Spell2.anm"
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.203947365
                            0.421052635
                            0.558781922
                            0.640216708
                            0.684512436
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0.214221165 }
                            { 1, 1, 1, 0.530837595 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.0412371121 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 62
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.534389436
                                0.690688372
                                1
                            }
                            values: list[f32] = {
                                0
                                0
                                0.125109747
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Passive_SmokeErode.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 0, 1, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -2 }
                miscRenderFlags: u8 = 1
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
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
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_W_Head_Teeth.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.25
                rate: embed = ValueFloat {
                    constantValue: f32 = 40
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0.0454545468
                                    0.584326029
                                    0.863871515
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.00598802418
                                    0.146147266
                                    0.46351254
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
                    10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "motes1"
                disabled: bool = true
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -500 }
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
                            { 0, 0, -500 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 120, 400 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                            values: list[vec3] = {
                                { 0, 120, 400 }
                            }
                        }
                    }
                    emitRotationAngles: list[embed] = {
                        ValueFloat {
                            constantValue: f32 = 180
                            dynamics: pointer = VfxAnimatedFloatVariableData {
                                probabilityTables: list[pointer] = {
                                    VfxProbabilityTableData {
                                        keyTimes: list[f32] = {
                                            0
                                            1
                                        }
                                        keyValues: list[f32] = {
                                            1.04999995
                                            0.949999988
                                        }
                                    }
                                }
                                times: list[f32] = {
                                    0
                                }
                                values: list[f32] = {
                                    180
                                }
                            }
                        }
                    }
                    emitRotationAxes: list[vec3] = {
                        { 0, 1.00000012, 0 }
                    }
                }
                particleColorTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/common_alpha_02.dds"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0912052095
                            0.139805824
                            0.322330087
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0, 0.0156862754, 0 }
                            { 1, 0.250980407, 0, 1 }
                            { 1, 0, 0.450980395, 1 }
                            { 0, 0.733333349, 1, 1 }
                            { 0, 0.482352942, 1, 1 }
                        }
                    }
                }
                pass: i16 = 9
                meshRenderFlags: u8 = 0
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
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
                    constantValue: vec3 = { 55, 1, 1 }
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
                            { 55, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0986526012
                            0.305438817
                            1
                        }
                        values: list[vec3] = {
                            { 5, 0, 0 }
                            { 1.63183522, 0, 0 }
                            { 0.627656758, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_SandFlecks.dds"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_colorGrad.dds"
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 1, 0, 0 }
                    }
                    paletteCount: i32 = 16
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.075000003
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                lifetime: option[f32] = {
                    2
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    0.5
                }
                emitterName: string = "on-ExtraTeeth"
                disabled: bool = true
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, -100 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Nunu_Base_Q_Bite_Mesh.scb"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.39000535 }
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
                            { 0.996078432, 0.996078432, 0.996078432, 1 }
                            { 0.340001523, 0.779995441, 0.820004582, 1 }
                            { 0.200000003, 0.889997721, 0.930006862, 0 }
                        }
                    }
                }
                pass: i16 = 101
                disableBackfaceCull: bool = true
                miscRenderFlags: u8 = 1
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -15, 270, 20 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1.5 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                        }
                        values: list[vec3] = {
                            { 0.600000024, 0.300000012, 0.600000024 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Nunu_Base_Q_BiteSwipe_V02.dds"
                texAddressModeBase: u8 = 2
                texDiv: vec2 = { 1, 0.670000017 }
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 1 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            0.400000006
                            1
                        }
                        values: list[vec2] = {
                            { 0, -0.200000003 }
                            { 0, 1 }
                            { 0, 10 }
                            { 0, 10 }
                        }
                    }
                }
                uvRotation: embed = ValueFloat {
                    constantValue: f32 = 180
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.25
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
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.192156866, 0.192156866, 0.286274523, 1 }
                            { 1, 1, 1, 0 }
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
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                particleLinger: option[f32] = {
                    0.400000006
                }
                lifetime: option[f32] = {
                    1
                }
                emitterLinger: option[f32] = {
                    1
                }
                emitterName: string = "LANDINGfLASH"
                Linger: pointer = VfxLingerDefinitionData {
                    UseLingerScale: flag = true
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.160297766
                            1
                        }
                        values: list[f32] = {
                            1
                            0
                            0
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.206888571
                            0.351583093
                            0.603550971
                            0.984782636
                        }
                        values: list[vec4] = {
                            { 0.156862751, 0.149019614, 0.250980407, 1 }
                            { 0.192156866, 0.192156866, 0.286274523, 0.988235295 }
                            { 0.596078455, 0.596078455, 0.890196085, 0.529411793 }
                            { 0.313725501, 0.541176498, 1, 0.184313729 }
                            { 1, 0.00392156886, 0.568627477, 0 }
                        }
                    }
                }
                pass: i16 = 301
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                -0.00973236002
                                0.119221412
                                0.309002429
                                0.649635017
                                0.824817538
                                0.987834573
                            }
                            values: list[f32] = {
                                0.0168067235
                                0.109243698
                                0.30252102
                                0.756302536
                                0.907563031
                                0.957983196
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Dissolve_Cloudy_01.dds"
                }
                depthBiasFactors: vec2 = { -1, -2 }
                miscRenderFlags: u8 = 1
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
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
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
                            1.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.349999994
                }
                emitterName: string = "SmallStarTrail"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 600, 300, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 5, 5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.25
                                }
                            }
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
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 100, -200 }
                }
                EmitterPosition: embed = ValueVector3 {
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
                            0.300000012
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.313725501, 0.541176498, 1, 1 }
                            { 0.600000024, 0.600000024, 0.889997721, 0.500007629 }
                            { 0.330006868, 0.330006868, 0.500007629, 0.500007629 }
                            { 0.160006106, 0.160006106, 0.2399939, 0.100007631 }
                        }
                    }
                }
                pass: i16 = 85
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 90 }
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
                            { 1, 0, 90 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 0, 0 }
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
                            { 60, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 1, 1 }
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
                            { 20, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/EnergyMote.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    2.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Subtractive"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0901960805, 0.0549019612, 0.196078435, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.300000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.0901960805, 0.0549019612, 0.196078435, 0 }
                            { 0.0901960805, 0.0549019612, 0.196078435, 1 }
                            { 0.0901960805, 0.0549019612, 0.196078435, 1 }
                            { 0.0901960805, 0.0549019612, 0.196078435, 0 }
                        }
                    }
                }
                pass: i16 = 999
                colorLookUpScales: vec2 = { 0.699999988, 0.800000012 }
                alphaRef: u8 = 0
                colorLookUpOffsets: vec2 = { 0.300000012, 0 }
                modulationFactor: vec4 = { 0.699999988, 1, 1, 1 }
                miscRenderFlags: u8 = 1
                stencilMode: u8 = 3
                stencilRef: u8 = 6
                isUniformScale: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 250, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0.25, 1 }
                            { 1, 4, 1 }
                            { 1.29999995, 4.32000017, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/ball32_02.dds"
            }
        }
        particleName: string = "Volibear_Skin16_W_Chomp"
        particlePath: string = "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_W_Chomp"
        flags: u16 = 198
        scaleDynamicallyWithAttachedBone: bool = true
    }
    "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Idle_ShoulderVFX02" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
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
                                    0.699999988
                                    1.29999995
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
                    0.200000003
                }
                emitterName: string = "Main_Shape_Clouds"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 300, 300 }
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 400, 300, 300 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 2, 4 }
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 35, 35 }
                }
                EmitterPosition: embed = ValueVector3 {
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
                                    0.800000012
                                    1
                                }
                            }
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
                    constantValue: vec4 = { 0.396078438, 0.396078438, 0.396078438, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.204167753
                            0.546286941
                            0.747704744
                            1
                        }
                        values: list[vec4] = {
                            { 0.233688399, 0.340626836, 0.372314334, 0 }
                            { 0.17427209, 0.178236812, 0.281216592, 0.200000003 }
                            { 0.175517112, 0.175517112, 0.372779697, 1 }
                            { 0.108727418, 0.121153407, 0.166197628, 0.101960786 }
                            { 0.0434909649, 0.0357247218, 0.0683429465, 0 }
                        }
                    }
                }
                pass: i16 = 20
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 3
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.119031653
                                0.641751826
                                1
                            }
                            values: list[f32] = {
                                -0.0481283404
                                -0.0802139044
                                0.966279805
                                3
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/LeeSin_Skin31_E_clouds_erosion_2.dds"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                useNavmeshMask: flag = true
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
                            VfxProbabilityTableData {}
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -15, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 230, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 230, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.549101591
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.953711808, 0.800000012, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/LeeSin_Skin31_E_clouds.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Mist.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
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
                timeBeforeFirstEmission: f32 = 0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
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
                                    1.5
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
                particleLinger: option[f32] = {
                    0.300000012
                }
                lifetime: option[f32] = {
                    3
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    2
                }
                emitterName: string = "Filler_Smoke"
                disabled: bool = true
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.25, 0 }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 200, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 200, 100 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 7, 2, 7 }
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
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 275
                    height: f32 = 10
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -25, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.510002315, 0.620004594, 1, 0.700007617 }
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.510002315, 0.620004594, 1, 0.700007617 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -999
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
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/alphaslice_mesh.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 1, 90 }
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
                            { 360, 1, 90 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 90, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 40, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 40, 40 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.649999976
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                            { 2, 2, 3 }
                            { 2, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Sion_Skin05_Sl_Dust_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
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
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "XY_DarkPlane"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.190005347, 0.190005347, 0.289997697, 1 }
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
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 75, 0.5 }
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
                            { 1, 1, 1 }
                            { 2, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Aura_Self.DDS"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "XY_Ringlight"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
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
                            { 0.192156866, 0.082891196, 0.230142266, 0.501960814 }
                            { 0.596078455, 0.257131875, 0.715647817, 1 }
                            { 0.192156866, 0.082891196, 0.230142266, 0.501960814 }
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
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 75, 0.5 }
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
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_Ringlight.dds"
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
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, -1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -10, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.5
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.190005347, 0.0819630921, 0.233135402, 0 }
                            { 0.600000024, 0.258823544, 0.715488374, 1 }
                            { 0.313725501, 0.233448684, 0.80392158, 1 }
                            { 1, 0.431372553, 0.80392158, 1 }
                            { 1, 0.431372553, 0.80392158, 0 }
                        }
                    }
                }
                pass: i16 = 6
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                0.5
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_Icon_Dissolve.dds"
                }
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 180 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 75, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_Icon.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Generic_SmokeScroll_Erosion.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "XY_Ringlight1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 2, -1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -10, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
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
                            { 1, 0.431372553, 0.80392158, 0.501960814 }
                            { 1, 0.431372553, 0.80392158, 1 }
                            { 1, 0.431372553, 0.80392158, 0.501960814 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 8
                colorLookUpTypeY: u8 = 3
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 180 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 27, 75, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_Icon.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "Basic"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
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
                EmitterPosition: embed = ValueVector3 {
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
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 0.509803951 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.431372553, 0.80392158, 0 }
                            { 1, 0.431372553, 0.80392158, 0.509803951 }
                            { 1, 0.431372553, 0.80392158, 0 }
                        }
                    }
                }
                depthBiasFactors: vec2 = { -1, -14 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 140, 70 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Riven_Skin23_Z_Glow.dds"
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
                                    0.5
                                    0.850000024
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
                emitterName: string = "SmolFlames"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -30, 25, 10 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 5, 0, 2 }
                }
                EmitterPosition: embed = ValueVector3 {
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
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.160006106, 0.0647042394, 0.200983465, 0 }
                            { 0.156862751, 0.0642829686, 0.201768562, 1 }
                            { 0.0800030529, 0.0345111191, 0.112550244, 0.500007629 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0
                                0.200000003
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_FlameFB_4x2_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 45, 0 }
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
                            { 90, 45, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 80, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
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
                            { 30, 80, 1 }
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
                            { 1.25, 0, 0 }
                            { 1, 1, 1 }
                            { 1.5, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_FlameFB_4x2.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 3, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 2 }
                    }
                }
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
                emitterName: string = "XY_Icon1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, -1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -20, 5, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.192156866, 0.192156866, 0.286274523, 1 }
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
                pass: i16 = 1
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 10
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 30, 180 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 30, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_R_Yasuo_Base_R_dash_sub.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_SoftEnergy_Ver.dds"
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
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "XY_Icon2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, -1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -25, 5, 5 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.190005347, 0.0819630921, 0.233135402, 0 }
                            { 0.7400015, 0.319216341, 0.715488374, 1 }
                            { 0.313725501, 0.233448684, 0.80392158, 1 }
                            { 0.192156866, 0.082891196, 0.230142266, 0.501960814 }
                            { 0.192156866, 0.082891196, 0.230142266, 0 }
                        }
                    }
                }
                pass: i16 = 9
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 10
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 25, 180 }
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
                            { -90, 25, 180 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_R_Yasuo_Base_R_dash_sub.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_SmokeyLicks.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                0.699999988
                            }
                            values: list[vec2] = {
                                { 1, 0.5 }
                                { 1, 0.100000001 }
                                { 1, 0.5 }
                            }
                        }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 120
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.119999997
                }
                emitterName: string = "Temp_Trail"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -300, 50, 100 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 80
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.890196085, 0.890196085, 0.890196085, 0 }
                            { 0.466666669, 0.466666669, 0.698039234, 1 }
                            { 0.313725501, 0.541176498, 1, 0.729411781 }
                            { 0.176470593, 0.176470593, 0.266666681, 0.43921569 }
                            { 0, 0, 0.200000003, 0.140001521 }
                        }
                    }
                }
                pass: i16 = 10
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -40 }
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Samira_Base_R_Smoke_Trail.dds"
                texDiv: vec2 = { 0.100000001, 1 }
                emitterUvScrollRate: vec2 = { -0.100000001, 0 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    0.400000006
                }
                lifetime: option[f32] = {
                    2.5
                }
                emitterName: string = "Temp_Trail1"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 450, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.980392158, 0.980392158, 0.980392158, 0 }
                            { 0.313725501, 0.541176498, 1, 1 }
                            { 0.333333343, 0.333333343, 0.498039216, 0.729411781 }
                            { 0.176470593, 0.176470593, 0.266666681, 0.43921569 }
                            { 0, 0, 0.200000003, 0.140001521 }
                        }
                    }
                }
                pass: i16 = 9
                alphaRef: u8 = 0
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Kassadin_Skin14_Q_WispTrail_Add.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                }
                texDiv: vec2 = { 2, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 120
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                emitterName: string = "Temp_Trail2"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 50, -100 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 80
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.156862751, 0.149019614, 0.250980407, 1 }
                }
                pass: i16 = -25
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -40 }
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 0.5, 1, 1 }
                            { 0.5, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Kassadin_Skin14_Q_WispTrail_Add.dds"
                texDiv: vec2 = { 0.200000003, 1 }
                emitterUvScrollRate: vec2 = { -0.100000001, 0 }
            }
        }
        particleName: string = "Volibear_Skin16_Idle_ShoulderVFX02"
        particlePath: string = "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Idle_ShoulderVFX02"
    }
    "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Idle_ShoulderVFX01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
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
                                    0.699999988
                                    1.29999995
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
                    0.200000003
                }
                emitterName: string = "Main_Shape_Clouds"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 300, 300 }
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 400, 300, 300 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 2, 4 }
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 35, 35 }
                }
                EmitterPosition: embed = ValueVector3 {
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
                                    0.800000012
                                    1
                                }
                            }
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
                    constantValue: vec4 = { 0.396078438, 0.396078438, 0.396078438, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.204167753
                            0.546286941
                            0.747704744
                            1
                        }
                        values: list[vec4] = {
                            { 0.233688399, 0.340626836, 0.372314334, 0 }
                            { 0.17427209, 0.178236812, 0.281216592, 0.200000003 }
                            { 0.175517112, 0.175517112, 0.372779697, 1 }
                            { 0.108727418, 0.121153407, 0.166197628, 0.101960786 }
                            { 0.0434909649, 0.0357247218, 0.0683429465, 0 }
                        }
                    }
                }
                pass: i16 = 20
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 3
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.119031653
                                0.641751826
                                1
                            }
                            values: list[f32] = {
                                -0.0481283404
                                -0.0802139044
                                0.966279805
                                3
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/LeeSin_Skin31_E_clouds_erosion_2.dds"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                useNavmeshMask: flag = true
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
                            VfxProbabilityTableData {}
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -15, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 230, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 230, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.549101591
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.953711808, 0.800000012, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/LeeSin_Skin31_E_clouds.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Mist.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
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
                timeBeforeFirstEmission: f32 = 0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
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
                                    1.5
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
                particleLinger: option[f32] = {
                    0.300000012
                }
                lifetime: option[f32] = {
                    3
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    2
                }
                emitterName: string = "Filler_Smoke"
                disabled: bool = true
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.25, 0 }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 200, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 200, 100 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 7, 2, 7 }
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
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 275
                    height: f32 = 10
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -25, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.510002315, 0.620004594, 1, 0.700007617 }
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.510002315, 0.620004594, 1, 0.700007617 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -999
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
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/alphaslice_mesh.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 1, 90 }
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
                            { 360, 1, 90 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 90, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 40, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 40, 40 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.649999976
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                            { 2, 2, 3 }
                            { 2, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Sion_Skin05_Sl_Dust_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
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
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "XY_DarkPlane"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.190005347, 0.190005347, 0.289997697, 1 }
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
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 75, 0.5 }
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
                            { 1, 1, 1 }
                            { 2, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Aura_Self.DDS"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "XY_Ringlight"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
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
                            { 0.192156866, 0.082891196, 0.230142266, 0.501960814 }
                            { 0.596078455, 0.257131875, 0.715647817, 1 }
                            { 0.192156866, 0.082891196, 0.230142266, 0.501960814 }
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
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 75, 0.5 }
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
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_Ringlight.dds"
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
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, -1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.5
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.190005347, 0.0819630921, 0.233135402, 0 }
                            { 0.600000024, 0.258823544, 0.715488374, 1 }
                            { 0.313725501, 0.233448684, 0.80392158, 1 }
                            { 1, 0.431372553, 0.80392158, 1 }
                            { 1, 0.431372553, 0.80392158, 0 }
                        }
                    }
                }
                pass: i16 = 6
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                0.5
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_Icon_Dissolve.dds"
                }
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 75, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_Icon.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Generic_SmokeScroll_Erosion.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "XY_Ringlight1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 2, -1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
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
                            { 1, 0.431372553, 0.80392158, 0.501960814 }
                            { 1, 0.431372553, 0.80392158, 1 }
                            { 1, 0.431372553, 0.80392158, 0.501960814 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 8
                colorLookUpTypeY: u8 = 3
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 27, 75, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_Icon.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "Basic"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
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
                EmitterPosition: embed = ValueVector3 {
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
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 0.509803951 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.431372553, 0.80392158, 0 }
                            { 1, 0.431372553, 0.80392158, 0.509803951 }
                            { 1, 0.431372553, 0.80392158, 0 }
                        }
                    }
                }
                depthBiasFactors: vec2 = { -1, -14 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 70, 140, 70 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Riven_Skin23_Z_Glow.dds"
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
                                    0.5
                                    0.850000024
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
                emitterName: string = "SmolFlames"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 25, -10 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 5, 0, 2 }
                }
                EmitterPosition: embed = ValueVector3 {
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
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.160006106, 0.0647042394, 0.200983465, 0 }
                            { 0.156862751, 0.0642829686, 0.201768562, 1 }
                            { 0.0800030529, 0.0345111191, 0.112550244, 0.500007629 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0
                                0.200000003
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_FlameFB_4x2_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 45, 0 }
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
                            { 90, 45, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 80, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
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
                            { 30, 80, 1 }
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
                            { 1.25, 0, 0 }
                            { 1, 1, 1 }
                            { 1.5, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_FlameFB_4x2.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 3, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 2 }
                    }
                }
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
                emitterName: string = "XY_Icon1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, -1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 5, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.192156866, 0.192156866, 0.286274523, 1 }
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
                pass: i16 = 1
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 10
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 30, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 30, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_R_Yasuo_Base_R_dash_sub.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_SoftEnergy_Ver.dds"
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
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "XY_Icon2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, -1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 5, -5 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.190005347, 0.0819630921, 0.233135402, 0 }
                            { 0.7400015, 0.319216341, 0.715488374, 1 }
                            { 0.313725501, 0.233448684, 0.80392158, 1 }
                            { 0.192156866, 0.082891196, 0.230142266, 0.501960814 }
                            { 0.192156866, 0.082891196, 0.230142266, 0 }
                        }
                    }
                }
                pass: i16 = 9
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 10
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 25, 0 }
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
                            { -90, 25, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_R_Yasuo_Base_R_dash_sub.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_SmokeyLicks.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                0.699999988
                            }
                            values: list[vec2] = {
                                { 1, 0.5 }
                                { 1, 0.100000001 }
                                { 1, 0.5 }
                            }
                        }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 120
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.119999997
                }
                emitterName: string = "Temp_Trail"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 50, -100 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 80
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.890196085, 0.890196085, 0.890196085, 0 }
                            { 0.466666669, 0.466666669, 0.698039234, 1 }
                            { 0.313725501, 0.541176498, 1, 0.729411781 }
                            { 0.176470593, 0.176470593, 0.266666681, 0.43921569 }
                            { 0, 0, 0.200000003, 0.140001521 }
                        }
                    }
                }
                pass: i16 = 10
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -40 }
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Samira_Base_R_Smoke_Trail.dds"
                texDiv: vec2 = { 0.100000001, 1 }
                emitterUvScrollRate: vec2 = { -0.100000001, 0 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    0.400000006
                }
                lifetime: option[f32] = {
                    2.5
                }
                emitterName: string = "Temp_Trail1"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 450, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.980392158, 0.980392158, 0.980392158, 0 }
                            { 0.313725501, 0.541176498, 1, 1 }
                            { 0.333333343, 0.333333343, 0.498039216, 0.729411781 }
                            { 0.176470593, 0.176470593, 0.266666681, 0.43921569 }
                            { 0, 0, 0.200000003, 0.140001521 }
                        }
                    }
                }
                pass: i16 = 9
                alphaRef: u8 = 0
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Kassadin_Skin14_Q_WispTrail_Add.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                }
                texDiv: vec2 = { 2, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 120
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                emitterName: string = "Temp_Trail2"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 50, -100 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 80
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.156862751, 0.149019614, 0.250980407, 1 }
                }
                pass: i16 = -25
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -40 }
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 0.5, 1, 1 }
                            { 0.5, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Kassadin_Skin14_Q_WispTrail_Add.dds"
                texDiv: vec2 = { 0.200000003, 1 }
                emitterUvScrollRate: vec2 = { -0.100000001, 0 }
            }
        }
        particleName: string = "Volibear_Skin16_Idle_ShoulderVFX01"
        particlePath: string = "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Idle_ShoulderVFX01"
    }
    "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Emote_PoroJoke" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6.9000001
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "bodyBlend_A"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "PORO"
                        }
                        mSubmeshesToDrawAlways: list[hash] = {
                            "PORO"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                pass: i16 = 40
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -6 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin16/Volibear_Skin16_Poro_TX_CM.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 160
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.150000006
                }
                emitterName: string = "Temp_Trail"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 600, 0 }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 450, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.890196085, 0.890196085, 0.890196085, 0 }
                            { 0.466666669, 0.466666669, 0.698039234, 1 }
                            { 0.313725501, 0.541176498, 1, 0.729411781 }
                            { 0.176470593, 0.176470593, 0.266666681, 0.43921569 }
                            { 0, 0, 0.200000003, 0.140001521 }
                        }
                    }
                }
                pass: i16 = 10
                alphaRef: u8 = 0
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Samira_Base_R_Smoke_Trail.dds"
                texDiv: vec2 = { 0.5, 1 }
                emitterUvScrollRate: vec2 = { -0.5, 0 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                emitterName: string = "Temp_Trail1"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 450, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.980392158, 0.980392158, 0.980392158, 0 }
                            { 0.313725501, 0.541176498, 1, 1 }
                            { 0.333333343, 0.333333343, 0.498039216, 0.729411781 }
                            { 0.176470593, 0.176470593, 0.266666681, 0.43921569 }
                            { 0, 0, 0.200000003, 0.140001521 }
                        }
                    }
                }
                pass: i16 = 9
                alphaRef: u8 = 0
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Kassadin_Skin14_Q_WispTrail_Add.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                }
                texDiv: vec2 = { 2, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0
                            0.5
                        }
                        values: list[f32] = {
                            12.5
                            25
                        }
                    }
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.699999988
                                    1.29999995
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
                    0.200000003
                }
                lifetime: option[f32] = {
                    2.5
                }
                emitterName: string = "Main_Shape_Clouds"
                disabled: bool = true
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.200000003, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 2, 6 }
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
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.00999999978
                }
                SpawnShape: pointer = VfxShapeSphere {
                    flags: u8 = 1
                }
                EmitterPosition: embed = ValueVector3 {
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
                                    0.800000012
                                    1
                                }
                            }
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
                    constantValue: vec4 = { 0.396078438, 0.396078438, 0.396078438, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.204167753
                            0.546286941
                            0.747704744
                            1
                        }
                        values: list[vec4] = {
                            { 0.233688399, 0.340626836, 0.372314334, 0 }
                            { 0.17427209, 0.178236812, 0.281216592, 0.500007629 }
                            { 0.175517112, 0.175517112, 0.372779697, 1 }
                            { 0.108727418, 0.121153407, 0.166197628, 0.101960786 }
                            { 0.0434909649, 0.0357247218, 0.0683429465, 0 }
                        }
                    }
                }
                pass: i16 = 20
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 3
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.119031653
                                0.641751826
                                1
                            }
                            values: list[f32] = {
                                -0.0481283404
                                -0.0802139044
                                0.966279805
                                3
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/LeeSin_Skin31_E_clouds_erosion_2.dds"
                }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRandomStartFrame: flag = true
                isRotationEnabled: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
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
                            VfxProbabilityTableData {}
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -15, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 125, 230, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 125, 230, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.549101591
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1, 0.800000012, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/LeeSin_Skin31_E_clouds.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Mist.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
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
                timeBeforeFirstEmission: f32 = 0.349999994
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
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
                                    0.200000003
                                    1.5
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
                    1.5
                }
                emitterName: string = "Embers"
                disabled: bool = true
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.5, 0 }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 300, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 1, 5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.25
                                }
                            }
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
                SpawnShape: pointer = VfxShapeSphere {
                    radius: f32 = 25
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 25 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.333333343, 0.333333343, 0.498039216, 0 }
                            { 0.474509805, 0.474509805, 0.564705908, 0.501960814 }
                            { 0.330006868, 0.330006868, 0.500007629, 1 }
                            { 0.141176477, 0.141176477, 0.211764708, 1 }
                            { 0.0627451017, 0.0627451017, 0.0941176489, 0 }
                        }
                    }
                }
                pass: i16 = 30
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isGroundLayer: flag = true
                useNavmeshMask: flag = true
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
                    constantValue: vec3 = { 300, 0, 0 }
                }
                directionVelocityScale: f32 = 0.00300000003
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 60, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 60, 60, 50 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.129999995
                            0.400000006
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.20000005, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 0.5, 1 }
                            { 1, 0.5, 1 }
                            { 0, 0, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Brand_Skin08_Q_StardustMoteAlpha.dds"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.899999976
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
                            1.5
                        }
                    }
                }
                particleLinger: option[f32] = {
                    1
                }
                lifetime: option[f32] = {
                    0.699999988
                }
                emitterName: string = "SmallStarTrail"
                disabled: bool = true
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -0.5, 0 }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 50, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 300, 50, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 1, 5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.25
                                }
                            }
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
                SpawnShape: pointer = VfxShapeSphere {
                    radius: f32 = 25
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 25 }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 0.596078455, 0.596078455, 0.890196085, 1 }
                            { 0.333333343, 0.333333343, 0.498039216, 1 }
                            { 0.160784319, 0.160784319, 0.239215687, 1 }
                        }
                    }
                }
                pass: i16 = 85
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, 90 }
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
                            { 1, 0, 90 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 0, 0 }
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
                            { 60, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 1, 1 }
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
                            { 20, 1, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 1.29999995, 1.29999995, 1.29999995 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/EnergyMote.dds"
            }
        }
        particleName: string = "Volibear_Skin16_Emote_PoroJoke"
        particlePath: string = "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Emote_PoroJoke"
        flags: u16 = 197
    }
    "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Idle_BackVFX01" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 25
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
                                    0.699999988
                                    1.29999995
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
                    0.200000003
                }
                emitterName: string = "Main_Shape_Clouds"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 400, 300, 300 }
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 400, 300, 300 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 2, 4 }
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 35, 35 }
                }
                EmitterPosition: embed = ValueVector3 {
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
                                    0.800000012
                                    1
                                }
                            }
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
                    constantValue: vec4 = { 0.396078438, 0.396078438, 0.396078438, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.204167753
                            0.546286941
                            0.747704744
                            1
                        }
                        values: list[vec4] = {
                            { 0.233688399, 0.340626836, 0.372314334, 0 }
                            { 0.17427209, 0.178236812, 0.281216592, 0.200000003 }
                            { 0.175517112, 0.175517112, 0.372779697, 1 }
                            { 0.108727418, 0.121153407, 0.166197628, 0.101960786 }
                            { 0.0434909649, 0.0357247218, 0.0683429465, 0 }
                        }
                    }
                }
                pass: i16 = 20
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 3
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.119031653
                                0.641751826
                                1
                            }
                            values: list[f32] = {
                                -0.0481283404
                                -0.0802139044
                                0.966279805
                                3
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.300000012
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/LeeSin_Skin31_E_clouds_erosion_2.dds"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                useNavmeshMask: flag = true
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
                            VfxProbabilityTableData {}
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { -15, 0, 0 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 230, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
                                    1.25
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, 230, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.549101591
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 0.953711808, 0.800000012, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/LeeSin_Skin31_E_clouds.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_Mist.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
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
                timeBeforeFirstEmission: f32 = 0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 15
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
                                    1.5
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
                particleLinger: option[f32] = {
                    0.300000012
                }
                lifetime: option[f32] = {
                    3
                }
                isSingleParticle: flag = true
                emitterLinger: option[f32] = {
                    2
                }
                emitterName: string = "Filler_Smoke"
                disabled: bool = true
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.25, 0 }
                }
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 200, 100 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 200, 100 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 7, 2, 7 }
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
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 275
                    height: f32 = 10
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -25, 0 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.510002315, 0.620004594, 1, 0.700007617 }
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
                                    0.800000012
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec4] = {
                            { 0.510002315, 0.620004594, 1, 0.700007617 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = -999
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
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/alphaslice_mesh.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                isGroundLayer: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 1, 90 }
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
                            { 360, 1, 90 }
                        }
                    }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 90, 0 }
                        }
                    }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 40, 40 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    1.5
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 30, 40, 40 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.649999976
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                            { 2, 2, 3 }
                            { 2, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Sion_Skin05_Sl_Dust_01.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
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
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "XY_DarkPlane"
                disabled: bool = true
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.190005347, 0.190005347, 0.289997697, 1 }
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
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 75, 0.5 }
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
                            { 1, 1, 1 }
                            { 2, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Aura_Self.DDS"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "XY_Ringlight"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.500007629 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
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
                            { 0.192156866, 0.082891196, 0.230142266, 0.501960814 }
                            { 0.596078455, 0.257131875, 0.715647817, 1 }
                            { 0.192156866, 0.082891196, 0.230142266, 0.501960814 }
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
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 35, 75, 0.5 }
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
                            { 2, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_Ringlight.dds"
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
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 24, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                            0.5
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.190005347, 0.0819630921, 0.233135402, 0 }
                            { 0.600000024, 0.258823544, 0.715488374, 1 }
                            { 0.313725501, 0.233448684, 0.80392158, 1 }
                            { 1, 0.431372553, 0.80392158, 1 }
                            { 1, 0.431372553, 0.80392158, 0 }
                        }
                    }
                }
                pass: i16 = 6
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                0.5
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_BackPiece01_Dissolve.dds"
                }
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 180 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -45, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 75, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_BackPiece01.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Generic_SmokeScroll_Erosion.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.5 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "XY_Ringlight1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 25, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.300007641 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
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
                            { 1, 0.431372553, 0.80392158, 0.501960814 }
                            { 1, 0.431372553, 0.80392158, 1 }
                            { 1, 0.431372553, 0.80392158, 0.501960814 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 8
                colorLookUpTypeY: u8 = 3
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 180 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -5, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 27, 75, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_BackPiece01.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "Basic"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 20, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
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
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 0.509803951 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.431372553, 0.80392158, 0 }
                            { 1, 0.431372553, 0.80392158, 0.509803951 }
                            { 1, 0.431372553, 0.80392158, 0 }
                        }
                    }
                }
                depthBiasFactors: vec2 = { -1, -14 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 100, 140, 70 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Riven_Skin23_Z_Glow.dds"
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
                                    0.5
                                    0.850000024
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
                emitterName: string = "SmolFlames"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { -60, 25, 60 }
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
                            { -60, 25, 60 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 5, 25, 2 }
                }
                EmitterPosition: embed = ValueVector3 {
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
                    constantValue: vec4 = { 1, 1, 1, 0.700007617 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.160006106, 0.0647042394, 0.200983465, 0 }
                            { 0.156862751, 0.0642829686, 0.201768562, 1 }
                            { 0.0800030529, 0.0345111191, 0.112550244, 0.500007629 }
                        }
                    }
                }
                colorLookUpTypeY: u8 = 3
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0
                                0.200000003
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_FlameFB_4x2_Dissolve.dds"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 45, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.800000012
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
                            { 30, 30, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_FlameFB_4x2.dds"
                numFrames: u16 = 6
                texDiv: vec2 = { 3, 2 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/color-hold.DDS"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 2 }
                    }
                }
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
                emitterName: string = "XY_Icon1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, -1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -20, 20, 0 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.192156866, 0.192156866, 0.286274523, 1 }
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
                pass: i16 = 1
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 10
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 180 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 30, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_R_Yasuo_Base_R_dash_sub.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_SoftEnergy_Ver.dds"
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
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    1
                }
                emitterName: string = "XY_Icon2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 0, -1 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -25, 20, 5 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.431372553, 0.80392158, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            0.850000024
                            1
                        }
                        values: list[vec4] = {
                            { 0.190005347, 0.0819630921, 0.233135402, 0 }
                            { 0.7400015, 0.319216341, 0.715488374, 1 }
                            { 0.313725501, 0.233448684, 0.80392158, 1 }
                            { 0.192156866, 0.082891196, 0.230142266, 0.501960814 }
                            { 0.192156866, 0.082891196, 0.230142266, 0 }
                        }
                    }
                }
                pass: i16 = 9
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 10
                depthBiasFactors: vec2 = { -1, -30 }
                particleIsLocalOrientation: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 180 }
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
                            { -90, 0, 180 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 30, 0.5 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_R_Yasuo_Base_R_dash_sub.dds"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Volibear_Skin07_Idle_SmokeyLicks.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                0.699999988
                            }
                            values: list[vec2] = {
                                { 1, 0.5 }
                                { 1, 0.100000001 }
                                { 1, 0.5 }
                            }
                        }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, 0.25 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 120
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.119999997
                }
                emitterName: string = "Temp_Trail"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 300, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -5, 20, 0 }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 80
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.890196085, 0.890196085, 0.890196085, 0 }
                            { 0.466666669, 0.466666669, 0.698039234, 1 }
                            { 0.313725501, 0.541176498, 1, 0.729411781 }
                            { 0.176470593, 0.176470593, 0.266666681, 0.43921569 }
                            { 0, 0, 0.200000003, 0.140001521 }
                        }
                    }
                }
                pass: i16 = 10
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -40 }
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Samira_Base_R_Smoke_Trail.dds"
                texDiv: vec2 = { 0.100000001, 1 }
                emitterUvScrollRate: vec2 = { -0.100000001, 0 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    0.400000006
                }
                lifetime: option[f32] = {
                    2.5
                }
                emitterName: string = "Temp_Trail1"
                disabled: bool = true
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 450, 0, 0 }
                        }
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.980392158, 0.980392158, 0.980392158, 0 }
                            { 0.313725501, 0.541176498, 1, 1 }
                            { 0.333333343, 0.333333343, 0.498039216, 0.729411781 }
                            { 0.176470593, 0.176470593, 0.266666681, 0.43921569 }
                            { 0, 0, 0.200000003, 0.140001521 }
                        }
                    }
                }
                pass: i16 = 9
                alphaRef: u8 = 0
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 0, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Kassadin_Skin14_Q_WispTrail_Add.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                }
                texDiv: vec2 = { 2, 1 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 120
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                emitterName: string = "Temp_Trail2"
                disabled: bool = true
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 500, 50, -100 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mCutoff: f32 = 80
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 800, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.156862751, 0.149019614, 0.250980407, 1 }
                }
                pass: i16 = -25
                alphaRef: u8 = 0
                depthBiasFactors: vec2 = { -1, -40 }
                particleIsLocalOrientation: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 60, 100, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0, 0 }
                            { 0.5, 1, 1 }
                            { 0.5, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Skin07/Particles/Kassadin_Skin14_Q_WispTrail_Add.dds"
                texDiv: vec2 = { 0.200000003, 1 }
                emitterUvScrollRate: vec2 = { -0.100000001, 0 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                emitterName: string = "Basic1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 27, 0 }
                }
                EmitterPosition: embed = ValueVector3 {
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
                depthBiasFactors: vec2 = { -1, -14 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 7, 140, 70 }
                }
                texture: string = "ASSETS/Characters/Volibear/Skins/Base/Particles/Volibear_Base_R_Yasuo_Base_R_dash_sub.dds"
            }
        }
        particleName: string = "Volibear_Skin16_Idle_BackVFX01"
        particlePath: string = "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Idle_BackVFX01"
        scaleDynamicallyWithAttachedBone: bool = true
    }
    "Characters/Volibear/Skins/Skin16/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Volibear_R_attack_buf_L" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_attack_buf_L"
            "Volibear_R_attack_buf_R" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_attack_buf_R"
            "Volibear_Passive_hitFlash_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_hitFlash_01"
            "Volibear_Idle_Breath" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Idle_Breath"
            "Volibear_R_Buf_Max" = "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_R_Buf_Max"
            "Volibear_R_disabledTower_A" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_disabledTower_A"
            "Volibear_R_Impact_Dust_A" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_R_Impact_Dust_A"
            "Volibear_Passive_maxStacks_Aura_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_maxStacks_Aura_01"
            0x86cad419 = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_cast"
            0x255cc173 = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_Q_hitDust"
            "Volibear_W_Chomp" = "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_W_Chomp"
            0x430a78d7 = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_hit"
            0xefccc0de = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_hit"
            "Volibear_W_hit_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_W_hit_01"
            "Volibear_BasicAttack_Swipe_R_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_BasicAttack_Swipe_R_01"
            "Volibear_BasicAttack_Swipe_L_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_BasicAttack_Swipe_L_01"
            "Volibear_BasicAttack_Hit_Left" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_BasicAttack_Hit_Left"
            "Volibear_BasicAttack_Hit_Right" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_BasicAttack_Hit_Right"
            "Volibear_E_AOE" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_E_AOE"
            "Volibear_E_AOE_Warning" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_E_AOE_Warning"
            "Volibear_E_AOE_Warning_Enemy" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_E_AOE_Warning_Enemy"
            "Volibear_R_AOE_Warning" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_AOE_Warning"
            "Volibear_Passive_zeroStacks_L_SpikeA" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_zeroStacks_L_SpikeA"
            "Volibear_Passive_zeroStacks_L_SpikeB" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_zeroStacks_L_SpikeB"
            "Volibear_Passive_zeroStacks_L_SpikeC" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_zeroStacks_L_SpikeC"
            "Volibear_Passive_zeroStacks_R_SpikeA" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_zeroStacks_R_SpikeA"
            "Volibear_Passive_zeroStacks_R_SpikeB" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_zeroStacks_R_SpikeB"
            "Volibear_Passive_zeroStacks_R_SpikeC" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_zeroStacks_R_SpikeC"
            "Volibear_Passive_maxStacks_L_SpikeA" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_maxStacks_L_SpikeA"
            "Volibear_Passive_maxStacks_L_SpikeB" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_maxStacks_L_SpikeB"
            "Volibear_Passive_maxStacks_L_SpikeC" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_maxStacks_L_SpikeC"
            "Volibear_Passive_maxStacks_R_SpikeA" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_maxStacks_R_SpikeA"
            "Volibear_Passive_maxStacks_R_SpikeB" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_maxStacks_R_SpikeB"
            "Volibear_Passive_maxStacks_R_SpikeC" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_maxStacks_R_SpikeC"
            "Volibear_Passive_midStacks_L_SpikeA" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_midStacks_L_SpikeA"
            "Volibear_Passive_midStacks_L_SpikeB" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_midStacks_L_SpikeB"
            "Volibear_Passive_midStacks_L_SpikeC" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_midStacks_L_SpikeC"
            "Volibear_Passive_midStacks_R_SpikeA" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_midStacks_R_SpikeA"
            "Volibear_Passive_midStacks_R_SpikeB" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_midStacks_R_SpikeB"
            "Volibear_Passive_midStacks_R_SpikeC" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_midStacks_R_SpikeC"
            "Volibear_E_cas" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_E_cas"
            "Volibear_Passive_midStacks_Aura_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_midStacks_Aura_01"
            "Volibear_Passive_zeroStacks_Aura_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_zeroStacks_Aura_01"
            "Volibear_E_Shield_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_E_Shield_01"
            "Volibear_W_Marked" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_W_Marked"
            0x46d2dfd3 = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_aura"
            0x6d78ac72 = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_R_aura_arc_01"
            "Volibear_Passive_chainLightning" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_chainLightning_01"
            0xbe6a7615 = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_pawsFront"
            0x9852d67e = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_pawPrints"
            0x4543e999 = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_ult_paws_L"
            0xead3c256 = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_Q_ult_runDust"
            0xacf17fa8 = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_ult_paws_R"
            "Volibear_R_thunderFist" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_thunderFist"
            "Volibear_R_thunderFist_Bolt" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_thunderFist_Bolt"
            "Volibear_Taunt_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Taunt_01"
            "Volibear_R_landingImpact_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_landingImpact_01"
            "Volibear_Idle_pawSpark" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Idle_pawSpark"
            "Volibear_R_leapGroundShadow" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_R_leapGroundShadow"
            "Volibear_E_wiggleSpark_01" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_E_wiggleSpark_01"
            0xd68d8ea4 = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_Q_pawSparks"
            "Volibear_W_Slash" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_W_Slash"
            "Volibear_W_Marked_Scratch" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_W_Marked_Scratch"
            "Volibear_E_Hit_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_E_Hit_01"
            0x631db25c = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Death_01"
            "Volibear_Death_02" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Death_02"
            "Volibear_Taunt_Swipe_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Taunt_Swipe_01"
            "Volibear_Taunt_Hit_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Taunt_Hit_01"
            "Volibear_Taunt_handGlow_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Taunt_handGlow_01"
            "Volibear_R_towerHit_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_towerHit_01"
            "Volibear_R_towerHitCrack_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_towerHitCrack_01"
            "Volibear_Recall_01" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_Recall_01"
            "Volibear_Recall_GroundRune_01" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_Recall_GroundRune_01"
            "Volibear_Recall_handSparks" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_Recall_handSparks"
            "Volibear_Recall_handSparks_L" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_Recall_handSparks_L"
            "Volibear_Recall_endBolt_01" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_Recall_endBolt_01"
            "Volibear_Recall_Roar_01" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_Recall_Roar_01"
            "Volibear_hitFlash_Crit" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_hitFlash_Crit"
            "Volibear_W_floatyRunes" = "Characters/Volibear/Skins/Skin3/Particles/Volibear_Base_W_floatyRunes"
            "Volibear_W_LifeSteal" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_W_LifeSteal"
            "Volibear_R_AOE_Warning_EnemyPOV" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_AOE_Warning_EnemyPOV"
            "Volibear_Q_BuffBreak" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_BuffBreak"
            "Volibear_Slow" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_Slow"
            "Volibear_Q_ShieldRune_L" = "Characters/Volibear/Skins/Skin0/Particles/Volibear_Base_Q_ShieldRune_L"
            "Volibear_Emote_PoroJoke" = "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Emote_PoroJoke"
            "Volibear_BasicAttack_Hit_Tower" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_BasicAttack_Hit_Tower"
            "Volibear_Emote_PoroJokeLoop" = "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Emote_PoroJokeLoop"
            "Volibear_Recall_Land" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Recall_Land"
            "Volibear_E_DragonChild" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_E_DragonChild"
            "Volibear_E_DragonChild_02" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_E_DragonChild_02"
            "Volibear_E_DragonChild_03" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_E_DragonChild_03"
            "Volibear_E_DragonChild_Negative" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_E_DragonChild_Negative"
            "Volibear_E_Spirit_Child01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_E_Spirit_Child01"
            "Volibear_E_Spirit_Child02" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_E_Spirit_Child02"
            "Volibear_Idle_ShoulderVFX01" = "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Idle_ShoulderVFX01"
            "Volibear_Idle_ShoulderVFX02" = "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Idle_ShoulderVFX02"
            "Volibear_Idle_BackVFX01" = "Characters/Volibear/Skins/Skin16/Particles/Volibear_Skin16_Idle_BackVFX01"
            "Volibear_Passive_MaxStacks_Swirl_Child" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_MaxStacks_Swirl_Child"
            "Volibear_Passive_MaxStacks_Swirl_Child02" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_MaxStacks_Swirl_Child02"
            "Volibear_Passive_chainLightning_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Passive_chainLightning_01"
            "Volibear_Q_aura" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_aura"
            "Volibear_Q_pawsFront" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_pawsFront"
            "Volibear_Q_cast" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_cast"
            "Volibear_Q_hit" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_hit"
            "Volibear_Q_ult_paws_L" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_ult_paws_L"
            "Volibear_Q_ult_paws_R" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Q_ult_paws_R"
            "Volibear_R_BackVFX01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_BackVFX01"
            "Volibear_R_ShoulderVFX01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_ShoulderVFX01"
            "Volibear_R_ShoulderVFX02" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_ShoulderVFX02"
            "Volibear_R_Slow" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_R_Slow"
            "Volibear_Emote_01_Joke_OnporoVFX" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_01_Joke_OnporoVFX"
            "Volibear_Emote_Taunt_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Taunt_01"
            "Volibear_Emote_Taunt_handGlow_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Taunt_handGlow_01"
            "Volibear_Emote_Taunt_Hit_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Taunt_Hit_01"
            "Volibear_Emote_Taunt_Swipe_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Taunt_Swipe_01"
            "Volibear_Death_01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Death_01"
            "Volibear_Emote_Recall_ONDragonVFX" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Recall_ONDragonVFX"
            "Volibear_Emote_Recall_Stompvfx" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Recall_Stompvfx"
            "Volibear_Emote_Recall_DragonBirthVFX" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Recall_DragonBirthVFX"
            "Volibear_Emote_Recall_Ending" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Recall_Ending"
            "Volibear_Emote_Recall_BackVFX01" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Recall_BackVFX01"
            "Volibear_Emote_Recall_SpiritSwirl" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Recall_SpiritSwirl"
            "Volibear_Emote_Recall_Spirit_Parent" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Recall_Spirit_Parent"
            "Volibear_Emote_Recall_Ending02" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Recall_Ending02"
            "Volibear_Emote_Recall_SpiritSwirl02" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Recall_SpiritSwirl02"
            "Volibear_Emote_Recall_Ending03" = "Characters/Volibear/Skins/Skin7/Particles/Volibear_Skin07_Emote_Recall_Ending03"
        }
    }
}
