#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Yasuo/Yasuo.bin"
    "DATA/Characters/Yasuo/Animations/Skin0.bin"
    "DATA/Yasuo_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin33_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin4_Skins_Skin40_Skins_Skin41_Skins_Skin42_Skins_Skin43_Skins_Skin44_Skins_Skin45_Skins_Skin46_Skins_Skin47_Skins_Skin48_Skins_Skin49_Skins_Skin5_Skins_Skin50_Skins_Skin51_Skins_Skin52_Skins_Skin53_Skins_Skin56_Skins_Skin57_Skins_Skin58_Skins_Skin59_Skins_Skin6_Skins_Skin60_Skins_Skin61_Skins_Skin62_Skins_Skin63_Skins_Skin64_Skins_Skin65_Skins_Skin66_Skins_Skin67_Skins_Skin68_Skins_Skin69_Skins_Skin7_Skins_Skin70_Skins_Skin71_Skins_Skin72_Skins_Skin73_Skins_Skin74_Skins_Skin75_Skins_Skin76_Skins_Skin77_Skins_Skin78_Skins_Skin79_Skins_Skin8_Skins_Skin80_Skins_Skin81_Skins_Skin82_Skins_Skin83_Skins_Skin84_Skins_Skin85_Skins_Skin86.bin"
    "DATA/Yasuo_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin40_Skins_Skin41_Skins_Skin42_Skins_Skin43_Skins_Skin44.bin"
}
entries: map[hash,embed] = {
    "Characters/Yasuo/Skins/Skin41" = SkinCharacterDataProperties {
        skinClassification: u32 = 2
        championSkinName: string = "YasuoSkin41"
        skinParent: i32 = 36
        metaDataTags: string = "gender:male,faction:ionia,race:human,element:wind,skinline:spiritblossom,subskinline:kanmei"
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Characters/Yasuo/Skins/Skin36/YasuoLoadscreen_36.tex"
        }
        loadscreenVintage: embed = CensoredImage {
            image: string = "ASSETS/Characters/Yasuo/Skins/Skin36/YasuoLoadscreen_36_LE.tex"
        }
        skinAudioProperties: embed = skinAudioProperties {
            tagEventList: list[string] = {
                "Yasuo"
            }
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "Yasuo_Base_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Yasuo/Skins/Base/Yasuo_Base_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Yasuo/Skins/Base/Yasuo_Base_SFX_events.bnk"
                    }
                }
                BankUnit {
                    name: string = "Yasuo_Base_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Yasuo/Skins/Base/Yasuo_Base_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Yasuo/Skins/Base/Yasuo_Base_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_Yasuo_Dance3D_buffactivate"
                        "Play_sfx_Yasuo_Dance3D_buffactivate_leadin"
                        "Play_sfx_Yasuo_Death3D_cast"
                        "Play_sfx_Yasuo_Joke3D_buffactivate"
                        "Play_sfx_Yasuo_Laugh3D_buffactivate"
                        "Play_sfx_Yasuo_Recall_windup"
                        "Play_sfx_Yasuo_Taunt23D_buffactivate"
                        "Play_sfx_Yasuo_Taunt3D_buffactivate"
                        "Play_sfx_Yasuo_YasuoBasicAttack2_OnCast"
                        "Play_sfx_Yasuo_YasuoBasicAttack2_OnHit"
                        "Play_sfx_Yasuo_YasuoBasicAttack3_OnCast"
                        "Play_sfx_Yasuo_YasuoBasicAttack3_OnHit"
                        "Play_sfx_Yasuo_YasuoBasicAttack4_OnCast"
                        "Play_sfx_Yasuo_YasuoBasicAttack4_OnHit"
                        "Play_sfx_Yasuo_YasuoBasicAttack5_OnCast"
                        "Play_sfx_Yasuo_YasuoBasicAttack5_OnHit"
                        "Play_sfx_Yasuo_YasuoBasicAttack6_OnCast"
                        "Play_sfx_Yasuo_YasuoBasicAttack6_OnHit"
                        "Play_sfx_Yasuo_YasuoBasicAttack_OnCast"
                        "Play_sfx_Yasuo_YasuoBasicAttack_OnHit"
                        "Play_sfx_Yasuo_YasuoCritAttack2_OnCast"
                        "Play_sfx_Yasuo_YasuoCritAttack2_OnHit"
                        "Play_sfx_Yasuo_YasuoCritAttack3_OnCast"
                        "Play_sfx_Yasuo_YasuoCritAttack3_OnHit"
                        "Play_sfx_Yasuo_YasuoCritAttack4_OnCast"
                        "Play_sfx_Yasuo_YasuoCritAttack4_OnHit"
                        "Play_sfx_Yasuo_YasuoCritAttack5_OnCast"
                        "Play_sfx_Yasuo_YasuoCritAttack5_OnHit"
                        "Play_sfx_Yasuo_YasuoCritAttack_OnCast"
                        "Play_sfx_Yasuo_YasuoCritAttack_OnHit"
                        "Play_sfx_Yasuo_YasuoDashWrapper_cast"
                        "Play_sfx_Yasuo_YasuoDashWrapper_hit"
                        "Play_sfx_Yasuo_YasuoEQComboSoundHit_OnBuffActivate"
                        "Play_sfx_Yasuo_YasuoEQComboSoundHit_OnHit"
                        "Play_sfx_Yasuo_YasuoPassiveMSShieldOn_buffdeactivate"
                        "Play_sfx_Yasuo_YasuoPassiveShield_OnBuffActivate"
                        "Play_sfx_Yasuo_YasuoQ2_OnCast"
                        "Play_sfx_Yasuo_YasuoQ3W_hit"
                        "Play_sfx_Yasuo_YasuoQ3W_missilelaunch"
                        "Play_sfx_Yasuo_YasuoQ3W_OnBuffActivate"
                        "Play_sfx_Yasuo_YasuoQ3W_OnBuffDeactivate"
                        "Play_sfx_Yasuo_YasuoQ3W_OnCast"
                        "Play_sfx_Yasuo_YasuoQ_hit"
                        "Play_sfx_Yasuo_YasuoQW_buffactivate"
                        "Play_sfx_Yasuo_YasuoQW_OnCast"
                        "Play_sfx_Yasuo_YasuoRDummySpell_OnCast"
                        "Play_sfx_Yasuo_YasuoRKnockUpCombo_hit_land"
                        "Play_sfx_Yasuo_YasuoRKnockUpCombo_OnBuffActivate"
                        "Play_sfx_Yasuo_YasuoRLeashParticle_buffactivate"
                        "Play_sfx_Yasuo_YasuoSheathSpark_buffactivate"
                        "Play_sfx_Yasuo_YasuoWindWallBuff_missilecast"
                        "Play_sfx_Yasuo_YasuoWMovingWall_buffactivate"
                        "Play_sfx_Yasuo_YasuoWMovingWall_hit"
                        "Play_sfx_Yasuo_YasuoWMovingWall_OnCast"
                        "Stop_sfx_Yasuo_YasuoDashWrapper_cast"
                        "Stop_sfx_Yasuo_YasuoEQComboSoundHit_OnBuffActivate"
                        "Stop_sfx_Yasuo_YasuoQ3W_OnBuffDeactivate"
                        "Stop_sfx_Yasuo_YasuoQW_buffactivate"
                        "Stop_sfx_Yasuo_YasuoRKnockUpCombo_OnBuffActivate"
                    }
                }
                BankUnit {
                    name: string = "Yasuo_Base_VO"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Yasuo/Skins/Base/Yasuo_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Yasuo/Skins/Base/Yasuo_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Yasuo/Skins/Base/Yasuo_Base_VO_audio.wpk"
                    }
                    events: list[string] = {
                        "Play_vo_Yasuo_Attack2DGeneral"
                        "Play_vo_Yasuo_Death3D"
                        "Play_vo_Yasuo_FirstEncounter3DMasterYi"
                        "Play_vo_Yasuo_FirstEncounter3DRiven"
                        "Play_vo_Yasuo_FirstEncounter3DShen"
                        "Play_vo_Yasuo_FirstEncounter3DYone"
                        "Play_vo_Yasuo_Joke3DGeneral"
                        "Play_vo_Yasuo_Kill3DYone"
                        "Play_vo_Yasuo_Laugh3DGeneral"
                        "Play_vo_Yasuo_Move2DFirstEnemyYone"
                        "Play_vo_Yasuo_Move2DStandard"
                        "Play_vo_Yasuo_Taunt3DGeneral"
                        "Play_vo_Yasuo_YasuoBasicAttack2_cast3D"
                        "Play_vo_Yasuo_YasuoBasicAttack3_cast3D"
                        "Play_vo_Yasuo_YasuoBasicAttack4_cast3D"
                        "Play_vo_Yasuo_YasuoBasicAttack5_cast3D"
                        "Play_vo_Yasuo_YasuoBasicAttack6_cast3D"
                        "Play_vo_Yasuo_YasuoBasicAttack_cast3D"
                        "Play_vo_Yasuo_YasuoCritAttack2_cast3D"
                        "Play_vo_Yasuo_YasuoCritAttack3_cast3D"
                        "Play_vo_Yasuo_YasuoCritAttack4_cast3D"
                        "Play_vo_Yasuo_YasuoCritAttack5_cast3D"
                        "Play_vo_Yasuo_YasuoCritAttack_cast3D"
                        "Play_vo_Yasuo_YasuoEDash_cast3D"
                        "Play_vo_Yasuo_YasuoQ1_cast3D"
                        "Play_vo_Yasuo_YasuoQ2_cast3D"
                        "Play_vo_Yasuo_YasuoQ3Wrapper_cast3D"
                        "Play_vo_Yasuo_YasuoR_cast3D"
                        "Play_vo_Yasuo_YasuoW_cast3D"
                    }
                    voiceOver: bool = true
                }
                BankUnit {
                    name: string = "Yasuo_Base_VO"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Yasuo/Skins/Base/Yasuo_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Yasuo/Skins/Base/Yasuo_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Yasuo/Skins/Base/Yasuo_Base_VO_audio.wpk"
                    }
                    events: list[string] = {
                        "Play_vo_Yasuo_Attack2DGeneral"
                        "Play_vo_Yasuo_Death3D"
                        "Play_vo_Yasuo_FirstEncounter3DMasterYi"
                        "Play_vo_Yasuo_FirstEncounter3DRiven"
                        "Play_vo_Yasuo_FirstEncounter3DShen"
                        "Play_vo_Yasuo_FirstEncounter3DYone"
                        "Play_vo_Yasuo_Joke3DGeneral"
                        "Play_vo_Yasuo_Kill3DYone"
                        "Play_vo_Yasuo_Laugh3DGeneral"
                        "Play_vo_Yasuo_Move2DFirstEnemyYone"
                        "Play_vo_Yasuo_Move2DStandard"
                        "Play_vo_Yasuo_Taunt3DGeneral"
                        "Play_vo_Yasuo_YasuoBasicAttack2_cast3D"
                        "Play_vo_Yasuo_YasuoBasicAttack3_cast3D"
                        "Play_vo_Yasuo_YasuoBasicAttack4_cast3D"
                        "Play_vo_Yasuo_YasuoBasicAttack5_cast3D"
                        "Play_vo_Yasuo_YasuoBasicAttack6_cast3D"
                        "Play_vo_Yasuo_YasuoBasicAttack_cast3D"
                        "Play_vo_Yasuo_YasuoCritAttack2_cast3D"
                        "Play_vo_Yasuo_YasuoCritAttack3_cast3D"
                        "Play_vo_Yasuo_YasuoCritAttack4_cast3D"
                        "Play_vo_Yasuo_YasuoCritAttack5_cast3D"
                        "Play_vo_Yasuo_YasuoCritAttack_cast3D"
                        "Play_vo_Yasuo_YasuoEDash_cast3D"
                        "Play_vo_Yasuo_YasuoQ1_cast3D"
                        "Play_vo_Yasuo_YasuoQ2_cast3D"
                        "Play_vo_Yasuo_YasuoQ3Wrapper_cast3D"
                        "Play_vo_Yasuo_YasuoR_cast3D"
                        "Play_vo_Yasuo_YasuoW_cast3D"
                    }
                    voiceOver: bool = true
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Yasuo/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Yasuo/Skins/Base/Yasuo.skl"
            simpleSkin: string = "ASSETS/Characters/Yasuo/Skins/Base/Yasuo.skn"
            texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Yasuo_base_TX_CM.dds"
	 	 	skinScale: f32 = 2
            selfIllumination: f32 = 0.699999988
            brushAlphaOverride: f32 = 0.5
            overrideBoundingBox: option[vec3] = {
                { 230, 180, 230 }
            }
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
            initialSubmeshToHide: string = "Yasuo_Instrument_Mat, Weapon_Trail"
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Yasuo/Skins/Base/Yasuo_Weapon_Trail_TX_CM.dds"
                    submesh: string = "Weapon_Trail"
                }
            }
        }
        idleParticlesEffects: list[embed] = {
            SkinCharacterDataProperties_CharacterIdleEffect {
                effectKey: hash = 0xe4c8d91f
                boneName: string = "root"
            }
        }
        armorMaterial: string = "Flesh"
        defaultAnimations: list[string] = {
            "Mask"
            "BottleFix_Skin01"
        }
        mContextualActionData: link = "Characters/Yasuo/CAC/Yasuo_Base"
        iconCircle: option[string] = {
            "ASSETS/Characters/Yasuo/HUD/Yasuo_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Yasuo/HUD/Yasuo_Square.tex"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 12
        }
        mResourceResolver: link = "Characters/Yasuo/Skins/Skin0/Resources"
    }
    "Characters/Yasuo/Skins/Skin41/Particles/Yasuo_Skin41_Z_Idle_ShoulderGlow" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLinger: option[f32] = {
                    1.5
                }
                emitterName: string = "DarkFlashAdd"
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
                    constantValue: vec4 = { 0, 0.86999315, 1, 0.280003041 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0, 0.86999315, 1, 0 }
                            { 0, 0.86999315, 1, 0.280003041 }
                            { 0, 0.86999315, 1, 0.280003041 }
                            { 0, 0.86999315, 1, 0 }
                        }
                    }
                }
                pass: i16 = 1
                depthBiasFactors: vec2 = { -0.200000003, -0.200000003 }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin36/Particles/Avatar_color_hold.dds"
                birthUvScrollRate: embed = ValueVector2 {
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
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 3, 3 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Yasuo/Skins/Skin41/Particles/Yasuo_Skin41_TX_ArmMask.dds"
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
                    1.5
                }
                emitterName: string = "DarkFlashAdd5"
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
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.5
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
                depthBiasFactors: vec2 = { -0.200000003, -0.200000003 }
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Recall_PixelBurst_color.dds"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 0.25 }
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
                            { 0.25, 0.25 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
                }
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Yasuo/Skins/Skin41/Particles/Yasuo_Skin41_TX_ArmMask.dds"
                }
            }
        }
        particleName: string = "Yasuo_Skin41_Z_Idle_ShoulderGlow"
        particlePath: string = "Characters/Yasuo/Skins/Skin41/Particles/Yasuo_Skin41_Z_Idle_ShoulderGlow"
    }
    "Characters/Yasuo/Skins/Skin41/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Yasuo_BA_Crit_hit_01" = 0x2c043169
            "Yasuo_BA_Crit_hit_02" = 0x29042cb0
            "Yasuo_BA_Crit_hit_03" = 0x2a042e43
            "Yasuo_BA_Crit_hit_04" = 0x2f043622
            "Yasuo_BA_hit_tar_01" = 0x6abec81e
            "Yasuo_BA_hit_tar_02" = 0x69bec68b
            "Yasuo_BA_hit_tar_03" = 0x68bec4f8
            "Yasuo_BA_hit_tar_04" = 0x6fbecffd
            "Yasuo_BA_trail_1" = 0x7713ce7d
            "Yasuo_BA_trail_2" = 0x7413c9c4
            "Yasuo_BA_trail_3" = 0x7513cb57
            "Yasuo_BA_trail_4" = 0x7213c69e
            "Yasuo_Dance_flute_wind" = 0xf28f09e2
            0x635797df = 0x9da31f9d
            "Yasuo_Emote_dance_in_sound" = 0x379e64bd
            "Yasuo_Emote_dance_sound" = 0xec35aa61
            "Yasuo_Emote_death_sound" = 0x642b6c20
            "Yasuo_Emote_joke_sound" = 0x1ced3ee9
            "Yasuo_Emote_laugh_sound" = 0x2f219447
            "Yasuo_Emote_taunt2_sound" = 0xf01b4a5c
            "Yasuo_Emote_taunt_generic" = 0xa72ac158
            "Yasuo_Emote_taunt_interactive_ninja" = 0x427e1f4e
            "Yasuo_Emote_taunt_interactive_riven" = 0xcf9e46d0
            "Yasuo_Emote_taunt_interactive_yi" = 0xee6ea130
            "Yasuo_Emote_taunt_sound" = 0xd526d1de
            "Yasuo_EQ3_cas" = 0x2149d794
            "Yasuo_EQ_cas" = 0x197d49db
            "Yasuo_EQ_SwordGlow" = 0x5f12ac4e
            "Yasuo_E_Dash" = 0x155830df
            "Yasuo_E_dash_hit" = 0x2cc239d5
            "Yasuo_E_timer1" = 0xe4b8e7ab
            "Yasuo_E_timer2" = 0xe5b8e93e
            "Yasuo_E_timer3" = 0xe6b8ead1
            "Yasuo_E_timer4" = 0xe7b8ec64
            "Yasuo_E_timer5" = 0xe8b8edf7
            "Yasuo_I_sheath_spark" = 0xa86b9f04
            "Yasuo_NightmareBot_E_timer1" = 0xe4b8e7ab
            "Yasuo_NightmareBot_E_timer2" = 0xe5b8e93e
            "Yasuo_NightmareBot_E_timer3" = 0xe6b8ead1
            "Yasuo_NightmareBot_E_timer4" = 0xe7b8ec64
            "Yasuo_NightmareBot_E_timer5" = 0xe8b8edf7
            "Yasuo_Passive_Activate" = 0xeb143788
            "Yasuo_Passive_Burst" = 0xbfa4e499
            "Yasuo_Q3_Hand" = 0x1b99786d
            "Yasuo_Q3_Indicator_Ring" = 0x1cb45094
            "Yasuo_Q3_Indicator_Ring_alt" = 0x86299480
            "Yasuo_Q_Hand" = 0x24d4d1a6
            "Yasuo_Q_hit_tar" = 0xa18d5244
            "Yasuo_Q_sound" = 0x92da76b6
            "Yasuo_Q_WindStrike" = 0xc552b523
            "Yasuo_Q_WindStrike_02" = 0xcb123a5a
            "Yasuo_Q_wind_hit_tar" = 0x356cbb33
            "Yasuo_Q_wind_mis" = 0xd11be9ad
            "Yasuo_Q_wind_ready_buff" = 0xb594aaa7
            0xc542e434 = 0x9572ed7a
            0x36a5a16b = 0x3abbc09d
            "Yasuo_R_cantcast_beam" = 0x1b967af5
            "Yasuo_R_cas_marker_01" = 0x64e82ada
            "Yasuo_R_CloneVFX" = 0x23622ccf
            "Yasuo_R_dash" = 0xed7dca54
            "Yasuo_R_impact_tar" = 0xa04155b6
            "Yasuo_R_indicator_beam" = 0x98a202d5
            "Yasuo_R_land_tar" = 0x4f6e91c5
            "Yasuo_R_slash_cas" = 0xd24a4b67
            "Yasuo_R_SwordGlow" = 0x58b91c58
            "Yasuo_R_tar_imp_01" = 0x6edc57c8
            0xf90ee152 = 0xb8c052bc
            0xf80edfbf = 0xbbc05775
            "Yasuo_Taunt_spit" = 0xb077c1b0
            "Yasuo_Wall_XinZhao_OLD" = 0x6aa6784b
            "Yasuo_W_windwall1" = 0x1c5ed0b6
            "Yasuo_W_windwall2" = 0x1b5ecf23
            "Yasuo_W_windwall3" = 0x1a5ecd90
            "Yasuo_W_windwall4" = 0x215ed895
            "Yasuo_W_windwall5" = 0x205ed702
            "Yasuo_W_windwall_activate" = 0x1c055e25
            "Yasuo_W_Windwall_big_impact" = 0xfe34bc6d
            "Yasuo_W_windwall_enemy_01" = 0x608fd4ea
            "Yasuo_W_windwall_enemy_02" = 0x5f8fd357
            "Yasuo_W_windwall_enemy_03" = 0x5e8fd1c4
            "Yasuo_W_windwall_enemy_04" = 0x5d8fd031
            "Yasuo_W_windwall_enemy_05" = 0x5c8fce9e
            "Yasuo_Q_Odyssey_Wandering_wind_mis" = 0xd11be9ad
            "Yasuo_Q_Odyssey_Growing_wind_mis" = 0xd11be9ad
            "Yasuo_Q_Odyssey_Wandering_Growing_wind_mis" = 0xd11be9ad
            0x79b5e280 = "Characters/Yasuo/Skins/Skin41/Particles/Yasuo_Skin41_Z_Idle_ShoulderGlow"
            0x87eb6a8f = 0xb7c0d7dd
            0x9c76d187 = 0x061302ad
            0x86e8ad4f = 0xf3fcbb2d
            0xd2537e8a = 0xa520575c
            0x3dd62ddb = 0xbabe985d
            0xd368cb74 = 0xd1863c8e
            0xd668d02d = 0xd0863afb
        }
    }
}
