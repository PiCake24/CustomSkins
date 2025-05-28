#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Chogath/Chogath.bin"
    "DATA/Chogath_Skins_Skin0_Skins_Skin1_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin6.bin"
    "DATA/Characters/Chogath/Animations/Skin0.bin"
    "DATA/Chogath_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin33_Skins_Skin34_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin4_Skins_Skin40_Skins_Skin6_Skins_Skin7.bin"
    "DATA/Chogath_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Chogath_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Chogath_Skins_Skin0_Skins_Skin1_Skins_Skin7.bin"
    "DATA/Characters/Chogath/Chogath.bin"
    "DATA/Characters/Chogath/Animations/Skin14.bin"
    "DATA/Chogath_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin33_Skins_Skin34_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin4_Skins_Skin40_Skins_Skin6_Skins_Skin7.bin"
    "DATA/Chogath_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin20_Skins_Skin21_Skins_Skin22.bin"
}
entries: map[hash,embed] = {
    "Characters/Chogath/Skins/Skin17" = SkinCharacterDataProperties {
        skinClassification: u32 = 1
        championSkinName: string = "Chogath"
        metaDataTags: string = "faction:void,gender:male,race:monster"
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Characters/Chogath/skins/base/ChogathLoadScreen.tex"
        }
        skinAudioProperties: embed = skinAudioProperties {
            tagEventList: list[string] = {
                "Chogath"
            }
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "Chogath_Base_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Chogath/Skins/Base/Chogath_Base_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Chogath/Skins/Base/Chogath_Base_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_Chogath_ChogathBasicAttack2_OnCast"
                        "Play_sfx_Chogath_ChogathBasicAttack2_OnHit"
                        "Play_sfx_Chogath_ChogathBasicAttack_OnCast"
                        "Play_sfx_Chogath_ChogathBasicAttack_OnHit"
                        "Play_sfx_Chogath_ChogathCritAttack_OnCast"
                        "Play_sfx_Chogath_ChogathCritAttack_OnHit"
                        "Play_sfx_Chogath_Feast_Cast_Anim"
                        "Play_sfx_Chogath_Feast_OnHit"
                        "Play_sfx_Chogath_FeralScream_hit"
                        "Play_sfx_Chogath_FeralScream_OnCast"
                        "Play_sfx_Chogath_Rupture_cast1"
                        "Play_sfx_Chogath_Rupture_cast2"
                        "Play_sfx_Chogath_Rupture_Cast_Anim"
                        "Play_sfx_Chogath_Rupture_OnCast"
                        "Play_sfx_Chogath_VorpalSpikes_buffactivate"
                        "Play_sfx_Chogath_VorpalSpikes_OnBuffDeactivate"
                        "Play_sfx_Chogath_VorpalSpikesMissle_hit"
                        "Play_sfx_Chogath_VorpalSpikesMissle_OnMissileLaunch"
                        "Play_sfx_ChogathEAttack_OnCast"
                    }
                }
                BankUnit {
                    name: string = "Chogath_Base_VO"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Chogath/Skins/Base/Chogath_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Chogath/Skins/Base/Chogath_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Chogath/Skins/Base/Chogath_Base_VO_audio.wpk"
                    }
                    events: list[string] = {
                        "Play_vo_Chogath_Attack2DGeneral"
                        "Play_vo_Chogath_Death3D"
                        "Play_vo_Chogath_Joke3DGeneral"
                        "Play_vo_Chogath_Laugh3DGeneral"
                        "Play_vo_Chogath_Move2DStandard"
                        "Play_vo_Chogath_Taunt3DGeneral"
                    }
                    voiceOver: bool = true
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = "Characters/Chogath/Animations/Skin0"
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Chogath/skins/base/Chogath.skl"
            simpleSkin: string = "ASSETS/Characters/Chogath/skins/base/Chogath.skn"
            texture: string = "ASSETS/Characters/Chogath/skins/base/GreenTerror.tex"
	 	 	skinScale: f32 = 2
            selfIllumination: f32 = 0.699999988
            overrideBoundingBox: option[vec3] = {
                { 130, 230, 130 }
            }
            initialSubmeshToHide: string = "HeadFrenzy FrenzyDaggers ShacklePieces ShackleBlades Crystal"
            reflectionFresnelColor: rgba = { 0, 0, 0, 255 }
        }
        armorMaterial: string = "Flesh"
        mContextualActionData: link = "Characters/Chogath/CAC/Chogath_Base"
        iconCircle: option[string] = {
            "ASSETS/Characters/Chogath/HUD/GreenTerror_Circle.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Chogath/HUD/GreenTerror_Square.tex"
        }
        healthBarData: embed = CharacterHealthBarDataRecord {
            unitHealthBarStyle: u8 = 12
        }
        mResourceResolver: link = "Characters/Chogath/Skins/Skin0/Resources"
    }
    "Characters/Chogath/Skins/Skin17/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Chogath_BA_tar" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_BA_tar"
            "Chogath_Death_SoundDust" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_Death_SoundDust"
            "Chogath_E_Cas" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_Cas"
            "Chogath_E_mis" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis"
            "Chogath_E_mis2" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis2"
            "Chogath_E_mis3" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis3"
            "Chogath_E_mis4" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis4"
            "Chogath_E_mis5" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis5"
            "Chogath_E_mis6" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis6"
            "Chogath_E_tar" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_tar"
            "Chogath_E_Tar02" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_Tar02"
            "Chogath_P_heal" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_P_heal"
            "Chogath_Q_Ally_team" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_Q_Ally_team"
            "Chogath_Q_cas" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_Q_cas"
            "Chogath_Q_Enemy_team" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_Q_Enemy_team"
            "Chogath_R_indicator" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_R_indicator"
            "Chogath_R_tar" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_R_tar"
            "Chogath_W_cas" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_W_cas"
            "Chogath_W_Sound01" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_W_Sound01"
            "Chogath_W_tar" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_W_tar"
            "Chogath_E_Cas_Spikes" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_Cas_Spikes"
            "Chogath_E_mis_child" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis_child"
            "Chogath_W_cas_child" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_W_cas_child"
            "Chogath_R_mis" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_R_mis"
            "Chogath_BA_Crit_tar" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_BA_Crit_tar"
            "Chogath_BA_tar" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_BA_tar"
            "Chogath_Death_SoundDust" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Death_SoundDust"
            "Chogath_E_mis" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_mis"
            "Chogath_E_mis2" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_mis2"
            "Chogath_E_mis3" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_mis3"
            "Chogath_E_mis4" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_mis4"
            "Chogath_E_mis5" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_mis5"
            "Chogath_E_mis6" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_mis6"
            "Chogath_E_tar" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_tar"
            "Chogath_E_Tar02" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_Tar02"
            "Chogath_P_heal" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_P_heal"
            "Chogath_Q_Ally_team" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Q_Ally_team"
            "Chogath_Q_cas" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Q_cas"
            "Chogath_Q_Enemy_team" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Q_Enemy_team"
            "Chogath_R_indicator" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_R_indicator"
            "Chogath_R_tar" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_R_tar"
            "Chogath_W_cas" = "Characters/Chogath/Skins/Skin17/Particles/Chogath_Skin17_W_cas"
            "Chogath_W_Sound01" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_W_Sound01"
            "Chogath_W_tar" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_W_tar"
            "Chogath_E_Cas_Spikes" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_Cas_Spikes"
            "Chogath_E_mis_child" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_mis_child"
            "Chogath_W_cas_child" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_W_cas_child"
            "Chogath_R_mis" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_R_mis"
            "Chogath_BA_Crit_tar" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_BA_Crit_tar"
            "Chogath_Q_beifeng" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Q_beifeng"
            "Chogath_E_mis_child_small" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_mis_child_small"
            "Chogath_E_mis_child_Zhong" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_mis_child_Zhong"
            "Chogath_R_tar_Child1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_R_tar_Child1"
            "Chogath_Recall_MountainMat" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Recall_MountainMat"
            "Chogath_E_mis_child_da" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_mis_child_da"
            "Chogath_E_mis_child_da_1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_mis_child_da_1"
            "Chogath_E_mis_child_da_2" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_mis_child_da_2"
            "Chogath_E_mis_child_da_3" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_mis_child_da_3"
            "Chogath_R_tar_Child2" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_R_tar_Child2"
            "Chogath_R_cas_child_1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_R_cas_child_1"
            "Chogath_W_cas_child_1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_W_cas_child_1"
            "Chogath_Idle_bei" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Idle_bei"
            "Chogath_Idle_bei_zilizi" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Idle_bei_zilizi"
            "Chogath_Q_beifeng_1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Q_beifeng_1"
            "Chogath_Idle_clould" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Idle_clould"
            "Chogath_Idle_clould2" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Idle_clould2"
            "Chogath_Idle_clould3" = "Characters/Chogath/Skins/Skin17/Particles/Chogath_Skin17_Idle_clould3"
            "Chogath_Idle_clould4" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Idle_clould4"
            "Chogath_Idle_bei_1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Idle_bei_1"
            "Chogath_Idle_wei" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Idle_wei"
            "Chogath_W_cas_child_2" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_W_cas_child_2"
            "Chogath_W_cas_child_3" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_W_cas_child_3"
            "Chogath_Recall_zui" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Recall_zui"
            "Chogath_Recall_MountainMat_1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Recall_MountainMat_1"
            "Chogath_Recall_MountainMat_2" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Recall_MountainMat_2"
            "Chogath_Recall_MountainMat_danshan" = "Characters/Chogath/Skins/Skin17/Particles/Chogath_Skin17_Recall_MountainMat_danshan"
            "Chogath_R_tar_1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_R_tar_1"
            "Chogath_Recall_ri" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Recall_ri"
            "Chogath_R_tar_Child1_1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_R_tar_Child1_1"
            "Chogath_Recall_zui_1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Recall_zui_1"
            "Chogath_E_Cas" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_Cas"
            0x92877c7c = "Characters/Chogath/Skins/Skin17/Particles/Chogath_Skin17_Emote_Recall_Outline"
        }
    }
    "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_Q_cas" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
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
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Smoke"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 250, 0 }
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
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 250, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 100
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.93333298, 0.992156982, 1 }
                            { 0.960784018, 0.525489986, 1, 1 }
                            { 0.286274999, 0.121569, 0.356862992, 0.298038989 }
                            { 0.0509800017, 0, 0.0980390012, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaRef: u8 = 64
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 165, 150, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.500100017
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
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
                                    1.5
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
                            { 165, 150, 30 }
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
                            { 0.600000024, 0.100000001, 0.600000024 }
                            { 0.800000012, 1.20000005, 0.800000012 }
                            { 1, 1.5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SmokeRay.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.300000012 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.899999976
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
                            0.899999976
                        }
                    }
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Smoke1"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 250, 0 }
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
                                    0.800000012
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 250, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 2, 0 }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    radius: f32 = 200
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.93333298, 0.992156982, 1 }
                            { 0.960784018, 0.525489986, 1, 1 }
                            { 0.286274999, 0.121569, 0.356862992, 0.298038989 }
                            { 0.0509800017, 0, 0.0980390012, 0 }
                        }
                    }
                }
                pass: i16 = 2
                alphaRef: u8 = 64
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 120, 120, 30 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.500100017
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -1
                                    1
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
                                    1.5
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
                            { 120, 120, 30 }
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
                            { 0.600000024, 0.100000001, 0.600000024 }
                            { 0.800000012, 1.20000005, 0.800000012 }
                            { 1, 1.5, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SmokeRay.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.300000012 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Temp_GroundGlow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.474509835 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.725489974, 0.525489986, 1, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.725489974, 0.525489986, 1, 0 }
                            { 0.725489974, 0.525489986, 1, 1 }
                            { 0.725489974, 0.525489986, 1, 1 }
                            { 0.725489974, 0.525489986, 1, 0 }
                        }
                    }
                }
                alphaRef: u8 = 0
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 1, 1, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                }
                                keyValues: list[f32] = {
                                    90
                                }
                            }
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
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 260, 260, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0500000007
                        }
                        values: list[vec3] = {
                            { 0.899999976, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_cas_Crack_03.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                lifetime: option[f32] = {
                    0.25
                }
                isSingleParticle: flag = true
                emitterName: string = "distort"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                particleColorTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_Distort_alpha_20.tex"
                blendMode: u8 = 1
                meshRenderFlags: u8 = 0
                distortionDefinition: pointer = VfxDistortionDefinitionData {
                    distortion: f32 = 0.0130000003
                    distortionMode: u8 = 2
                    normalMapTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_distortion_soundwaves_01.tex"
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 360, 360, 360 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.100000001, 0.100000001, 0.100000001 }
                            { 1.20000005, 1.20000005, 1.20000005 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_AuraSelf.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    2.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Pop1"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.800000012, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.800000012, 0, 1 }
                            { 1, 0.800000012, 0, 0 }
                        }
                    }
                }
                pass: i16 = 31
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Star.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
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
                                    0.25
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
                    0.200000003
                }
                isSingleParticle: flag = true
                emitterName: string = "Rocks_UP"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 25, 1500, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 25, 1500, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 3, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -800, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -800, 0 }
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 250
                    height: f32 = 1
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.568627477, 0.529411793, 0.474509835, 1 }
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    0.5
                                    0.500100017
                                    1
                                }
                                keyValues: list[f32] = {
                                    -1
                                    -0.5
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
                            { 90, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 50 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    3
                                }
                            }
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 5, 5, 50 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0.5
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_rockshards.tex"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                particleLinger: option[f32] = {
                    2.5
                }
                lifetime: option[f32] = {
                    1.10000002
                }
                isSingleParticle: flag = true
                emitterName: string = "Pop"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0, 0.533333004, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0, 0.533333004, 1 }
                            { 1, 0, 0.533333004, 0 }
                        }
                    }
                }
                pass: i16 = 31
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 300, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Glow.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    2.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "glow1"
                blendMode: u8 = 4
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0, 0.568627, 0.368627012 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0, 0.568627, 0.368627012 }
                            { 1, 0, 0.568627, 0 }
                        }
                    }
                }
                pass: i16 = 31
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 450, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Glow.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 30
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
                                    0.75
                                    1.64999998
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
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "GroundDust_Wisps"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 1200, 50, 0 }
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
                            { 1200, 50, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 6, 6 }
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 0, 15, 0 }
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
                                { 0, 15, 0 }
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
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, -25 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.568627, 0.529411972, 0.474510014, 0.447059005 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.5
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 0.568627, 0.529411972, 0.474510014, 0.447059005 }
                            { 0.568627, 0.529411972, 0.474510014, 0.447059005 }
                            { 0.568627, 0.529411972, 0.474510014, 0.447059005 }
                            { 0.568627, 0.529411972, 0.474510014, 0.447059005 }
                            { 0.568627, 0.529411972, 0.474510014, 0 }
                        }
                    }
                }
                pass: i16 = 30
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    beginIn: f32 = 10
                    deltaIn: f32 = 30
                }
                depthBiasFactors: vec2 = { -1, -100 }
                isGroundLayer: flag = true
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
                    constantValue: vec3 = { 9, 0, 0 }
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
                            { 9, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 45, 45, 45 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 45, 45, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                            { 2, 2, 2 }
                            { 3, 3, 3 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Spirit_Explosion.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.150000006, 0.349999994 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.150000006, 0.349999994 }
                        }
                    }
                }
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
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Swirl.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.600000024, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.600000024, 0.5 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.600000024
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.64999998
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.600000024
                        }
                    }
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "UpDust_Wisps"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 200, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 7, 0 }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 60
                    height: f32 = 40
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.568627, 0.529411972, 0.474510014, 0.450980008 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.501452446
                            0.73329705
                            0.926652133
                            1
                        }
                        values: list[vec4] = {
                            { 0.568627, 0.529411972, 0.474510014, 0.450980008 }
                            { 0.568627, 0.529411972, 0.474510014, 0.450980008 }
                            { 0.568627, 0.529411972, 0.474510014, 0.386772692 }
                            { 0.568627, 0.529411972, 0.474510014, 0.163575798 }
                            { 0.568627, 0.529411972, 0.474510014, 0.0336324088 }
                            { 0.568627, 0.529411972, 0.474510014, 0 }
                        }
                    }
                }
                pass: i16 = 15
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 80, 1 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 80, 1 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1.5, 1.5, 1 }
                            { 4.5, 6, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Spirit_Explosion.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.150000006, 0.349999994 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.150000006, 0.349999994 }
                        }
                    }
                }
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
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Swirl.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.600000024, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.600000024, 0.5 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.0666000023
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                particleLinger: option[f32] = {
                    10.75
                }
                lifetime: option[f32] = {
                    0.466600001
                }
                isSingleParticle: flag = true
                emitterName: string = "Dark_BG"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.890196145 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.0627449974, 0, 0.301961005, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 0.0627449974, 0, 0.301961005, 1 }
                            { 0.0627449974, 0, 0.301961005, 1 }
                            { 0.0627449974, 0, 0.301961005, 0 }
                        }
                    }
                }
                pass: i16 = -50
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -90, 0 }
                }
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 350, 152, 152 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Glow.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.75
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    2.04999995
                }
                isSingleParticle: flag = true
                emitterName: string = "Smaller_Inner"
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -150, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Spikes02.scb"
                    }
                }
                blendMode: u8 = 3
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.835294008, 0.00392200006, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                0.5
                                1
                            }
                            values: list[f32] = {
                                2
                                0
                                0
                                2
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Dissolve.tex"
                    erosionMapAddressMode: u8 = 0
                }
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -20, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2.5, 2 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.140000001
                            0.349999994
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 0.899999976, 0, 0.899999976 }
                            { 0.899999976, 0, 0.899999976 }
                            { 1, 1.5, 1 }
                            { 1, 1.5, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 350
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
                                    0.25
                                    1.5
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
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "Dark Flakes"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -0.300000012, 0 }
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
                            { 0, -0.300000012, 0 }
                        }
                    }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -75, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -150, 0 }
                        }
                    }
                }
                emissionMeshScale: f32 = 2
                emissionMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Spikes01.scb"
                SpawnShape: pointer = VfxShapeLegacy {
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
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.439993888 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            0.999000013
                        }
                        values: list[vec4] = {
                            { 0.917647064, 0, 1, 0 }
                            { 1, 0.0470588244, 0.952941179, 1 }
                            { 0.325490206, 0.0705882385, 0.31764707, 1 }
                            { 0.0509803928, 0, 0.0941176489, 0 }
                        }
                    }
                }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 20, 2 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.999000013
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeFlakes.tex"
                frameRate: f32 = 18
                numFrames: u16 = 36
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_W_Cas_Gradient.tex"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    paletteSelector: embed = ValueVector3 {
                        constantValue: vec3 = { 2, 2, 2 }
                    }
                    paletteCount: i32 = 2
                }
                texDiv: vec2 = { 6, 6 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    2.06500006
                }
                isSingleParticle: flag = true
                emitterName: string = "Big_Outer_Anim"
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -90, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Spikes01_Skinned.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Spikes01_Skinned.skl"
                        mAnimationName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Spikes01_Skinned.anm"
                    }
                }
                blendMode: u8 = 3
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.835294008, 0.00392200006, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0557008013
                                0.23565723
                                1
                            }
                            values: list[f32] = {
                                2
                                0
                                0
                                2
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Dissolve.tex"
                    erosionMapAddressMode: u8 = 0
                }
                uvScrollClamp: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2.5, 2 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.300000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 350
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
                                    0.25
                                    1.5
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
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    0.5
                }
                emitterName: string = "Bright1"
                birthOrbitalVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -0.300000012, 0 }
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
                            { 0, -0.300000012, 0 }
                        }
                    }
                }
                birthAcceleration: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -75, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -150, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -150, 0 }
                        }
                    }
                }
                emissionMeshScale: f32 = 2
                emissionMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Spikes01.scb"
                SpawnShape: pointer = VfxShapeLegacy {
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
                        { 1.00000012, 0, 0 }
                        { 0, 1.00000012, 0 }
                    }
                }
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.850003839, 0, 1, 0.650003791 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                            0.999000013
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.572549045, 0.254901975, 0.615686297, 1 }
                            { 0, 0, 0, 0 }
                        }
                    }
                }
                isRandomStartFrame: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 5, 5 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeFlakes.tex"
                frameRate: f32 = 18
                numFrames: u16 = 36
                texDiv: vec2 = { 6, 6 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1.5
                }
                particleLinger: option[f32] = {
                    0.5
                }
                lifetime: option[f32] = {
                    2.06500006
                }
                isSingleParticle: flag = true
                emitterName: string = "Big_Outer_Anim_TWIST"
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -90, 0 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Spikes01_Skinned.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Spikes01_Skinned.skl"
                        mAnimationName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Spikes01_Skinned_Twist.anm"
                    }
                }
                blendMode: u8 = 3
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.835294008, 0.00392200006, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.0557008013
                                0.23565723
                                1
                            }
                            values: list[f32] = {
                                2
                                0
                                0
                                2
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 1.79999995
                    erosionMapName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Dissolve.tex"
                    erosionMapAddressMode: u8 = 0
                }
                uvScrollClamp: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -10, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 2.5, 2 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1.64999998
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
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "UpDust_Wisps_Color"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 1200, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 1200, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 6, 0 }
                }
                SpawnShape: pointer = VfxShapeCylinder {
                    flags: u8 = 1
                    radius: f32 = 60
                    height: f32 = 40
                }
                primitive: pointer = VfxPrimitiveRay {}
                blendMode: u8 = 4
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.25
                            0.501452446
                            0.743464053
                            0.926652133
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 0, 1 }
                            { 1, 0.770000756, 0.059998475, 0.931010067 }
                            { 1, 0.280003041, 0.130006865, 0.855255783 }
                            { 0.600000024, 0.259998471, 1, 0.382207215 }
                            { 0.400000006, 0.0500038154, 1, 0.0628790706 }
                            { 0.400000006, 0, 1, 0 }
                        }
                    }
                }
                pass: i16 = 15
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { -90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 40, 80, 1 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 40, 80, 1 }
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
                            { 1, 1, 1 }
                            { 3, 6, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Spirit_Explosion.tex"
                uvMode: u8 = 2
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_W_Cas_Gradient.tex"
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.150000006, 0.349999994 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.150000006, 0.349999994 }
                        }
                    }
                }
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
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Swirl.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.600000024, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.600000024, 0.5 }
                            }
                        }
                    }
                }
            }
        }
        particleName: string = "Chogath_Base_Q_cas"
        particlePath: string = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_Q_cas"
        soundOnCreateDefault: string = "Play_sfx_Chogath_Rupture_cast2"
    }
    "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis2" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "spike_1"
                        "spike_2"
                        "spike_3"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Tripple Spike"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 80 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.10000002, 1.10000002, 1.10000002 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "single_spike"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Single Spike"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 90 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeSingle_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeSingle_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 0.899999976, 0.899999976 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
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
                                    0.5
                                    1
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
                particleLinger: option[f32] = {
                    0.649999976
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "ShapesAdd"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                birthDrag: embed = ValueVector3 {
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0.5, 0 }
                            { 0, 1, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 100, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 100 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.360006094 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.360006094 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.305737108
                            0.5
                            0.851125658
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.149019614, 0.988235295, 0 }
                            { 0.898039222, 0.117647059, 1, 1 }
                            { 0.912829161, 0.16076906, 1, 0.935593247 }
                            { 0.940001547, 0.2399939, 1, 0.519996941 }
                            { 0.348732412, 0.222923845, 1, 0.0813559294 }
                            { 0.0980392173, 0.215686277, 1, 0 }
                        }
                    }
                }
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
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.89999998
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
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
                    constantValue: vec3 = { 9, 0, 0 }
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
                            { 9, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 70, 45 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 70, 45 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_DirectionalShapes_2x4.tex"
                numFrames: u16 = 8
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    paletteCount: i32 = 2
                }
                texDiv: vec2 = { 2, 4 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Swirl.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.600000024, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.600000024, 0.5 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.649999976
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.75
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "DUST_Nebula_Smoke"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 100, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 100 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.549019635, 0.325490206, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.568627, 0.529411972, 0.474510014, 0.462745011 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.568627, 0.529411972, 0.474510014, 0.462745011 }
                            { 0.568627, 0.529411972, 0.474510014, 0 }
                        }
                    }
                }
                depthBiasFactors: vec2 = { -1, -100 }
                isGroundLayer: flag = true
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
                    constantValue: vec3 = { 9, 0, 0 }
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
                            { 9, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 85, 85, 45 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 85, 85, 45 }
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
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Spirit_Explosion.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.150000006, 0.349999994 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.150000006, 0.349999994 }
                        }
                    }
                }
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
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Swirl.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.600000024, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.600000024, 0.5 }
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
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    2.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "BG_Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -150, 100 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.109803997, 0.0117650004, 0.439215988, 0.618996978 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 0.109803997, 0.0117650004, 0.439215988, 0.618996978 }
                            { 0.109803997, 0.0117650004, 0.439215988, 0 }
                        }
                    }
                }
                pass: i16 = -5
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 450, 250, 1 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Glow.tex"
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
                                    0.699999988
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
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Streaks"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 135, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 80 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.498039007, 0.200000003, 0.937255025, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.0781238973, 0, 0.191126928, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.074217774, 0.0298040006, 0.139669746, 1 }
                        }
                    }
                }
                pass: i16 = 10
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
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
                            { 3, 3, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.300000012, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 0.200000003, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Darkness.tex"
            }
        }
        particleName: string = "Chogath_Base_E_mis2"
        particlePath: string = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis2"
    }
    "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis3" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "spike_1"
                        "spike_2"
                        "spike_3"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Tripple"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 80 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.20000005, 1.20000005, 1.20000005 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "single_spike"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Single 1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 35, 120, 130 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                                        0.25
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 35, 120, 130 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeSingle_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeSingle_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.10000002, 1.10000002, 1.10000002 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "single_spike"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Single 2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -35, 120, 130 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {}
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
                                        0.25
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { -35, 120, 130 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeSingle_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeSingle_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.10000002, 1.10000002, 1.10000002 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
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
                                    0.5
                                    1
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
                particleLinger: option[f32] = {
                    0.649999976
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "ShapesAdd"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                birthDrag: embed = ValueVector3 {
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0.5, 0 }
                            { 0, 1, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 120, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 100 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.360006094 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.360006094 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.305737108
                            0.5
                            0.851125658
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.149019614, 0.988235295, 0 }
                            { 0.898039222, 0.117647059, 1, 1 }
                            { 0.912829161, 0.16076906, 1, 0.935593247 }
                            { 0.940001547, 0.2399939, 1, 0.519996941 }
                            { 0.348732412, 0.222923845, 1, 0.0813559294 }
                            { 0.0980392173, 0.215686277, 1, 0 }
                        }
                    }
                }
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
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.89999998
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
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
                    constantValue: vec3 = { 9, 0, 0 }
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
                            { 9, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 70, 45 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 70, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.04999995, 1.04999995, 1 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_DirectionalShapes_2x4.tex"
                numFrames: u16 = 8
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    paletteCount: i32 = 2
                }
                texDiv: vec2 = { 2, 4 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Swirl.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.600000024, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.600000024, 0.5 }
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
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    2.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "BG_Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -150, 100 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.109803997, 0.0117650004, 0.439215988, 0.618996978 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 0.109803997, 0.0117650004, 0.439215988, 0.618996978 }
                            { 0.109803997, 0.0117650004, 0.439215988, 0 }
                        }
                    }
                }
                pass: i16 = -5
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 450, 250, 1 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Glow.tex"
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
                                    0.699999988
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
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Streaks"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 135, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 80 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.498039007, 0.200000003, 0.937255025, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.0781238973, 0, 0.191126928, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.074217774, 0.0298040006, 0.139669746, 1 }
                        }
                    }
                }
                pass: i16 = 10
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
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
                            { 3, 3, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.300000012, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 0.200000003, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Darkness.tex"
            }
        }
        particleName: string = "Chogath_Base_E_mis3"
        particlePath: string = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis3"
    }
    "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis4" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "spike_1"
                        "spike_2"
                        "spike_3"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Tripple"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 80, 80 }
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
                                { 50, 80, 80 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.20000005, 1.20000005, 1.20000005 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "spike_1"
                        "spike_2"
                        "spike_3"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Tripple1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -50, 80, 80 }
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
                                { -50, 80, 80 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.20000005, 1.20000005, 1.20000005 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
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
                                    0.5
                                    1
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
                particleLinger: option[f32] = {
                    0.649999976
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "ShapesAdd"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                birthDrag: embed = ValueVector3 {
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0.5, 0 }
                            { 0, 1, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 140, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 100 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.360006094 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.360006094 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.305737108
                            0.5
                            0.851125658
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.149019614, 0.988235295, 0 }
                            { 0.898039222, 0.117647059, 1, 1 }
                            { 0.912829161, 0.16076906, 1, 0.935593247 }
                            { 0.940001547, 0.2399939, 1, 0.519996941 }
                            { 0.348732412, 0.222923845, 1, 0.0813559294 }
                            { 0.0980392173, 0.215686277, 1, 0 }
                        }
                    }
                }
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
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.89999998
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
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
                    constantValue: vec3 = { 9, 0, 0 }
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
                            { 9, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 70, 45 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 70, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.20000005, 1.20000005, 1 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_DirectionalShapes_2x4.tex"
                numFrames: u16 = 8
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    paletteCount: i32 = 2
                }
                texDiv: vec2 = { 2, 4 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Swirl.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.600000024, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.600000024, 0.5 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.649999976
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.75
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "DUST_Nebula_Smoke"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 100, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 100 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.549019635, 0.325490206, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.568627, 0.529411972, 0.474510014, 0.462745011 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.568627, 0.529411972, 0.474510014, 0.462745011 }
                            { 0.568627, 0.529411972, 0.474510014, 0 }
                        }
                    }
                }
                depthBiasFactors: vec2 = { -1, -100 }
                isGroundLayer: flag = true
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
                    constantValue: vec3 = { 9, 0, 0 }
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
                            { 9, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 85, 85, 45 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 85, 85, 45 }
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
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Spirit_Explosion.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.150000006, 0.349999994 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.150000006, 0.349999994 }
                        }
                    }
                }
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
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Swirl.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.600000024, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.600000024, 0.5 }
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
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    2.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "BG_Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -150, 100 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.109803997, 0.0117650004, 0.439215988, 0.618996978 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 0.109803997, 0.0117650004, 0.439215988, 0.618996978 }
                            { 0.109803997, 0.0117650004, 0.439215988, 0 }
                        }
                    }
                }
                pass: i16 = -5
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 450, 250, 1 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Glow.tex"
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
                                    0.699999988
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
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Streaks"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 135, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 80 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.498039007, 0.200000003, 0.937255025, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.0781238973, 0, 0.191126928, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.074217774, 0.0298040006, 0.139669746, 1 }
                        }
                    }
                }
                pass: i16 = 10
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
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
                            { 3, 3, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.300000012, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 0.200000003, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Darkness.tex"
            }
        }
        particleName: string = "Chogath_Base_E_mis4"
        particlePath: string = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis4"
    }
    "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis5" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "spike_1"
                        "spike_2"
                        "spike_3"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Tripple"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 70, 80, 80 }
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
                                { 70, 80, 80 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.20000005, 1.20000005, 1.20000005 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "spike_1"
                        "spike_2"
                        "spike_3"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Tripple1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -70, 80, 80 }
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
                                { -70, 80, 80 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.20000005, 1.20000005, 1.20000005 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "single_spike"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Single"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 80, 120, 130 }
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
                                        0.25
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 80, 120, 130 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeSingle_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeSingle_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.10000002, 1.10000002, 1.10000002 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 110
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
                                    0.5
                                    1
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
                particleLinger: option[f32] = {
                    0.649999976
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "ShapesAdd"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                birthDrag: embed = ValueVector3 {
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0.5, 0 }
                            { 0, 1, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 175, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 100 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.360006094 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.360006094 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.305737108
                            0.5
                            0.851125658
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.149019614, 0.988235295, 0 }
                            { 0.898039222, 0.117647059, 1, 1 }
                            { 0.912829161, 0.16076906, 1, 0.935593247 }
                            { 0.940001547, 0.2399939, 1, 0.519996941 }
                            { 0.348732412, 0.222923845, 1, 0.0813559294 }
                            { 0.0980392173, 0.215686277, 1, 0 }
                        }
                    }
                }
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
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.89999998
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
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
                    constantValue: vec3 = { 9, 0, 0 }
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
                            { 9, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 70, 45 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 70, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.29999995, 1.29999995, 1 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_DirectionalShapes_2x4.tex"
                numFrames: u16 = 8
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    paletteCount: i32 = 2
                }
                texDiv: vec2 = { 2, 4 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Swirl.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.600000024, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.600000024, 0.5 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.649999976
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.75
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "DUST_Nebula_Smoke"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 100, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 100 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.549019635, 0.325490206, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.568627, 0.529411972, 0.474510014, 0.462745011 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.568627, 0.529411972, 0.474510014, 0.462745011 }
                            { 0.568627, 0.529411972, 0.474510014, 0 }
                        }
                    }
                }
                depthBiasFactors: vec2 = { -1, -100 }
                isGroundLayer: flag = true
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
                    constantValue: vec3 = { 9, 0, 0 }
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
                            { 9, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 85, 85, 45 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 85, 85, 45 }
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
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Spirit_Explosion.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.150000006, 0.349999994 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.150000006, 0.349999994 }
                        }
                    }
                }
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
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Swirl.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.600000024, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.600000024, 0.5 }
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
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    2.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "BG_Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -150, 100 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.109803997, 0.0117650004, 0.439215988, 0.618996978 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 0.109803997, 0.0117650004, 0.439215988, 0.618996978 }
                            { 0.109803997, 0.0117650004, 0.439215988, 0 }
                        }
                    }
                }
                pass: i16 = -5
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 450, 250, 1 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Glow.tex"
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
                                    0.699999988
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
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Streaks"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 135, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 80 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.498039007, 0.200000003, 0.937255025, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.0781238973, 0, 0.191126928, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.074217774, 0.0298040006, 0.139669746, 1 }
                        }
                    }
                }
                pass: i16 = 10
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
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
                            { 3, 3, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.300000012, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 0.200000003, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Darkness.tex"
            }
        }
        particleName: string = "Chogath_Base_E_mis5"
        particlePath: string = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis5"
    }
    "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis6" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "spike_1"
                        "spike_2"
                        "spike_3"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Tripple"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 50, 80, 80 }
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
                                { 50, 80, 80 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.29999995, 1.29999995, 1.29999995 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "spike_1"
                        "spike_2"
                        "spike_3"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Tripple1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -50, 80, 80 }
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
                                { -50, 80, 80 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.29999995, 1.29999995, 1.29999995 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "single_spike"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Single"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { -80, 120, 130 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
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
                                        0.25
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { -80, 120, 130 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeSingle_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeSingle_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.10000002, 1.10000002, 1.10000002 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "single_spike"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Single1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeLegacy {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 80, 120, 130 }
                        dynamics: pointer = VfxAnimatedVector3fVariableData {
                            probabilityTables: list[pointer] = {
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
                                        0.25
                                        1
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 80, 120, 130 }
                            }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeSingle_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeSingle_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.10000002, 1.10000002, 1.10000002 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
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
                                    0.5
                                    1
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
                particleLinger: option[f32] = {
                    0.649999976
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "ShapesAdd"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                birthDrag: embed = ValueVector3 {
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0.5, 0 }
                            { 0, 1, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 200, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 100 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.360006094 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.360006094 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.305737108
                            0.5
                            0.851125658
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.149019614, 0.988235295, 0 }
                            { 0.898039222, 0.117647059, 1, 1 }
                            { 0.912829161, 0.16076906, 1, 0.935593247 }
                            { 0.940001547, 0.2399939, 1, 0.519996941 }
                            { 0.348732412, 0.222923845, 1, 0.0813559294 }
                            { 0.0980392173, 0.215686277, 1, 0 }
                        }
                    }
                }
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
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.89999998
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
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
                    constantValue: vec3 = { 9, 0, 0 }
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
                            { 9, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 70, 45 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 70, 45 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.5, 1.5, 1 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_DirectionalShapes_2x4.tex"
                numFrames: u16 = 8
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    paletteCount: i32 = 2
                }
                texDiv: vec2 = { 2, 4 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Swirl.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.600000024, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.600000024, 0.5 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.649999976
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.75
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "DUST_Nebula_Smoke"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 100, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 100 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.549019635, 0.325490206, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.568627, 0.529411972, 0.474510014, 0.462745011 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.568627, 0.529411972, 0.474510014, 0.462745011 }
                            { 0.568627, 0.529411972, 0.474510014, 0 }
                        }
                    }
                }
                depthBiasFactors: vec2 = { -1, -100 }
                isGroundLayer: flag = true
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
                    constantValue: vec3 = { 9, 0, 0 }
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
                            { 9, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 85, 85, 45 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 85, 85, 45 }
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
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Spirit_Explosion.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.150000006, 0.349999994 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.150000006, 0.349999994 }
                        }
                    }
                }
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
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Swirl.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.600000024, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.600000024, 0.5 }
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
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    2.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "BG_Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -150, 100 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.109803997, 0.0117650004, 0.439215988, 0.618996978 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 0.109803997, 0.0117650004, 0.439215988, 0.618996978 }
                            { 0.109803997, 0.0117650004, 0.439215988, 0 }
                        }
                    }
                }
                pass: i16 = -5
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 450, 250, 1 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Glow.tex"
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
                                    0.699999988
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
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Streaks"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 135, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 80 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.498039007, 0.200000003, 0.937255025, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.0781238973, 0, 0.191126928, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.074217774, 0.0298040006, 0.139669746, 1 }
                        }
                    }
                }
                pass: i16 = 10
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
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
                            { 3, 3, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.300000012, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 0.200000003, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Darkness.tex"
            }
        }
        particleName: string = "Chogath_Base_E_mis6"
        particlePath: string = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis6"
    }
    "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
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
                                    0.5
                                    1
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
                particleLinger: option[f32] = {
                    0.649999976
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "ShapesAdd"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
                }
                birthDrag: embed = ValueVector3 {
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
                                    1
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0, 0.5, 0 }
                            { 0, 1, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 100, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 100 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.360006094 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.360006094 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.305737108
                            0.5
                            0.851125658
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.149019614, 0.988235295, 0 }
                            { 0.898039222, 0.117647059, 1, 1 }
                            { 0.912829161, 0.16076906, 1, 0.935593247 }
                            { 0.940001547, 0.2399939, 1, 0.519996941 }
                            { 0.348732412, 0.222923845, 1, 0.0813559294 }
                            { 0.0980392173, 0.215686277, 1, 0 }
                        }
                    }
                }
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
                                1
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionSliceWidth: f32 = 1.89999998
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
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
                    constantValue: vec3 = { 9, 0, 0 }
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
                            { 9, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 80, 70, 45 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 80, 70, 45 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_DirectionalShapes_2x4.tex"
                numFrames: u16 = 8
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    palleteSrcMixColor: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                    paletteCount: i32 = 2
                }
                texDiv: vec2 = { 2, 4 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Swirl.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.600000024, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.600000024, 0.5 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.649999976
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.75
                                    1
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.649999976
                        }
                    }
                }
                particleLinger: option[f32] = {
                    0.75
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "DUST_Nebula_Smoke"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 100, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 100 }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.549019635, 0.325490206, 1, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.568627, 0.529411972, 0.474510014, 0.462745011 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec4] = {
                            { 0.568627, 0.529411972, 0.474510014, 0.462745011 }
                            { 0.568627, 0.529411972, 0.474510014, 0 }
                        }
                    }
                }
                depthBiasFactors: vec2 = { -1, -100 }
                isGroundLayer: flag = true
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
                    constantValue: vec3 = { 9, 0, 0 }
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
                            { 9, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 85, 85, 45 }
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 85, 85, 45 }
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
                            { 1, 1, 1 }
                            { 2, 2, 2 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Spirit_Explosion.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.150000006, 0.349999994 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0
                                    2
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0.150000006, 0.349999994 }
                        }
                    }
                }
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
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/base/Particles/Rakan_Skin01_Swirl.tex"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0.600000024, 0.5 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            probabilityTables: list[pointer] = {
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        0.349999994
                                        -0.200000003
                                    }
                                }
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.600000024, 0.5 }
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
                    constantValue: f32 = 0.699999988
                }
                particleLinger: option[f32] = {
                    2.5
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "BG_Glow"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, -150, 100 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.109803997, 0.0117650004, 0.439215988, 0.618996978 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 0.109803997, 0.0117650004, 0.439215988, 0.618996978 }
                            { 0.109803997, 0.0117650004, 0.439215988, 0 }
                        }
                    }
                }
                pass: i16 = -5
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 90 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 450, 250, 1 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Glow.tex"
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
                                    0.699999988
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
                    1
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Streaks"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 50, 0 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 135, 100, 50 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 80 }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.498039007, 0.200000003, 0.937255025, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.300000012
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.0781238973, 0, 0.191126928, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.498039007, 0.200000003, 0.937255025, 1 }
                            { 0.074217774, 0.0298040006, 0.139669746, 1 }
                        }
                    }
                }
                pass: i16 = 10
                miscRenderFlags: u8 = 1
                isDirectionOriented: flag = true
                birthRotation0: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    0.5
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
                            { 3, 3, 0 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.800000012
                            1
                        }
                        values: list[vec3] = {
                            { 1, 0.300000012, 1 }
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1, 0.200000003, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Z_Darkness.tex"
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
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_E_mis_child"
                        }
                    }
                    boneToSpawnAt: list[string] = {
                        "spike_1"
                        "spike_2"
                        "spike_3"
                    }
                    childrenProbability: embed = ValueFloat {
                        constantValue: f32 = 0.5
                    }
                }
                emitterName: string = "Tripple"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 0, 80 }
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_E_Mis_SpikeTripple_MESH.skl"
                    }
                }
                blendMode: u8 = 1
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
                            { 0, 360, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.899999976, 0.899999976, 0.899999976 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_SpikeText.tex"
                paletteDefinition: pointer = VfxPaletteDefinitionData {
                    paletteTexture: string = "ASSETS/Characters/Chogath/skins/base/Particles/Chogath_Base_Q_Cas_SpikeGradient.tex"
                }
            }
        }
        particleName: string = "Chogath_Base_E_mis"
        particlePath: string = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis"
    }
    "Characters/Chogath/Skins/Skin17/Materials/Ink_Body_inst" = StaticMaterialDef {
        name: string = "Characters/Chogath/Skins/Skin17/Materials/Ink_Body_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "Diffuse_Texture"
                texturePath: string = "ASSETS/Characters/Chogath/skins/Skin17/Chogath_Skin17_TX_CM.tex"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Swapped_Texture"
                texturePath: string = "ASSETS/Shared/Materials/white.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Ink_Texture"
                texturePath: string = "ASSETS/Characters/Chogath/skins/Skin14/Chogath_Skin14_Ink_Mask.tex"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Ink_Color_Texture"
                texturePath: string = "ASSETS/Shared/Materials/black.SKINS_Ivern_Skin30.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Alpha"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TexDissolveBias"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "LightenDiff"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "HardOutlineSize"
                value: vec4 = { 3, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "HardOutline_Softness"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "HardOutline_Smooth_Step"
                value: vec4 = { 0.0500000007, 0.0599999987, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "DissolveBias"
                value: vec4 = { -1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "SmoothStep"
                value: vec4 = { 0, 0.649999976, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Ink_Color"
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Color"
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "TEX_SWAP"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_ALPHA"
            }
            StaticMaterialSwitchDef {
                name: string = "DEFINE_INK_COLOR_BY_TEXTURE"
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
                        shader: link = "Shaders/SkinnedMesh/HKG_InkOutline"
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
        dynamicMaterial: pointer = DynamicMaterialDef {
            parameters: list[embed] = {
                DynamicMaterialParameterDef {
                    name: string = "DissolveBias"
                    driver: pointer = SwitchMaterialDriver {
                        mElements: list[embed] = {
                            SwitchMaterialDriverElement {
                                mCondition: pointer = HasBuffDynamicMaterialBoolDriver {
                                    mScriptName: string = "recall"
                                }
                                mValue: pointer = LerpMaterialDriver {
                                    mBoolDriver: pointer = DelayedBoolMaterialDriver {
                                        mBoolDriver: pointer = HasBuffDynamicMaterialBoolDriver {
                                            mScriptName: string = "recall"
                                        }
                                        mDelayOn: f32 = 4
                                    }
                                    mOnValue: f32 = -1
                                    mOffValue: f32 = -2
                                    mTurnOnTimeSec: f32 = 2.5
                                }
                            }
                        }
                        mDefaultValue: pointer = FloatLiteralMaterialDriver {
                            mValue: f32 = 1
                        }
                    }
                }
            }
        }
    }
    "Characters/Chogath/Skins/Skin17/Materials/Ink_Prop_inst" = StaticMaterialDef {
        name: string = "Characters/Chogath/Skins/Skin17/Materials/Ink_Prop_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "Diffuse_Texture"
                texturePath: string = "ASSETS/Characters/Chogath/skins/Skin17/Chogath_Skin17_Recall_TX_CM.tex"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Swapped_Texture"
                texturePath: string = "ASSETS/Characters/Chogath/skins/Skin17/Chogath_Skin17_Recall_TX_CM.tex"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Ink_Texture"
                texturePath: string = "ASSETS/Characters/Chogath/skins/Skin14/Chogath_Skin14_Ink_Mask.tex"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Ink_Color_Texture"
                texturePath: string = "ASSETS/Shared/Materials/black.SKINS_Ivern_Skin30.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Alpha"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "TexDissolveBias"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "LightenDiff"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "HardOutlineSize"
                value: vec4 = { 3, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "HardOutline_Softness"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "HardOutline_Smooth_Step"
                value: vec4 = { 0.0500000007, 0.0599999987, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "DissolveBias"
                value: vec4 = { -1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "SmoothStep"
                value: vec4 = { 0, 0.649999976, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Ink_Color"
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Color"
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "TEX_SWAP"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "USE_ALPHA"
            }
            StaticMaterialSwitchDef {
                name: string = "DEFINE_INK_COLOR_BY_TEXTURE"
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
                        shader: link = "Shaders/SkinnedMesh/HKG_InkOutline"
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
        dynamicMaterial: pointer = DynamicMaterialDef {
            parameters: list[embed] = {
                DynamicMaterialParameterDef {
                    name: string = "DissolveBias"
                    driver: pointer = SwitchMaterialDriver {
                        mElements: list[embed] = {
                            SwitchMaterialDriverElement {
                                mCondition: pointer = HasBuffDynamicMaterialBoolDriver {
                                    mScriptName: string = "recall"
                                }
                                mValue: pointer = LerpMaterialDriver {
                                    mBoolDriver: pointer = DelayedBoolMaterialDriver {
                                        mBoolDriver: pointer = HasBuffDynamicMaterialBoolDriver {
                                            mScriptName: string = "recall"
                                        }
                                        mDelayOn: f32 = 4
                                    }
                                    mOnValue: f32 = -1
                                    mOffValue: f32 = 1
                                    mTurnOnTimeSec: f32 = 2.5
                                }
                            }
                        }
                        mDefaultValue: pointer = FloatLiteralMaterialDriver {
                            mValue: f32 = 1
                        }
                    }
                }
                DynamicMaterialParameterDef {
                    name: string = "Alpha"
                    driver: pointer = LerpMaterialDriver {
                        mBoolDriver: pointer = HasBuffDynamicMaterialBoolDriver {
                            mScriptName: string = "recall"
                        }
                        mTurnOffTimeSec: f32 = 0
                    }
                }
            }
        }
    }
    "Characters/Chogath/Skins/Skin17/Materials/ChoGath_Skin17_FlowMap_Bloom_inst" = StaticMaterialDef {
        name: string = "Characters/Chogath/Skins/Skin17/Materials/ChoGath_Skin17_FlowMap_Bloom_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "FlowMap"
                texturePath: string = "ASSETS/Characters/Chogath/skins/Skin14/Chogath_skin14_FM.tex"
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Diffuse_Texture"
                texturePath: string = "ASSETS/Characters/Chogath/skins/Skin17/Chogath_Skin17_TX_CM.tex"
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Mask"
                texturePath: string = "ASSETS/Characters/Chogath/skins/Skin14/ChoGath_Skin14_TX_CM_Mask.tex"
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Anim_Scale_Intensity"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Anim_Scale_Frequency"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Anim_Scale_Speed"
                value: vec4 = { 0.174999997, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Anim_Wave_Speed"
                value: vec4 = { 0.300000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Anim_Wave_Dir"
                value: vec4 = { 1, 1, 8, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Anim_Wave_Frequency"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "FlowIntensity"
                value: vec4 = { 0.150000006, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "FlowSpeed"
                value: vec4 = { 0.400000006, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "BloomColorIntensity"
                value: vec4 = { 3.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Color_Intensity"
                value: vec4 = { 8, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "BloomColor"
                value: vec4 = { 0, 0.580392182, 0.694117665, 0.20784314 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Fresnel"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Color"
                value: vec4 = { 0, 0.34117648, 0.407843143, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Noise_Tiling_Speed"
                value: vec4 = { 1, 3, 0.200000003, -0.100000001 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Anim_Wave_Dir_Intensity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "HardOutlineSize"
                value: vec4 = { 1.10000002, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "OutLine_Intensity"
                value: vec4 = { 0.282000005, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "OutLine_Color"
                value: vec4 = { 0, 0.0666666701, 0.0901960805, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Alpha_Control"
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "ALPHA"
            }
            StaticMaterialSwitchDef {
                name: string = "APPLY_FLOWMAP_TO_ALPHA"
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
                        shader: link = "Shaders/SkinnedMesh/HKG_Diff_Flowmap_Bloom"
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
    "Characters/Chogath/Skins/Skin17/Particles/Chogath_Skin17_Emote_Recall_Outline" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                lifetime: option[f32] = {
                    100
                }
                emitterName: string = "Outline"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 110, 0 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
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
                            { 1, 0.730006874, 0.269993126, 0 }
                            { 1, 0.439993888, 0.110002287, 0 }
                            { 1, 0.37000075, 0.160006106, 0 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                isUniformScale: flag = true
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
                                    0
                                    8
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 190, 1, 1 }
                }
                materialOverrideDefinitions: list[embed] = {
                    VfxMaterialOverrideDefinitionData {
                        subMeshName: option[string] = {
                            "Body"
                        }
                        material: link = "Characters/Chogath/Skins/Skin17/Materials/Ink_Body_inst"
                    }
                }
            }
        }
        particleName: string = "Chogath_Skin17_Emote_Recall_Outline"
        particlePath: string = "Characters/Chogath/Skins/Skin17/Particles/Chogath_Skin17_Emote_Recall_Outline"
        flags: u16 = 134
    }
    "Characters/Chogath/Skins/Skin17/Particles/Chogath_Skin17_Recall_MountainMat_danshan" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = -0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Center_ALpha19"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 30, 5 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.skl"
                        mAnimationName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.anm"
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.533333361, 0.431372553, 0.431372553, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.159999996
                            0.5
                            0.600000024
                            0.680000007
                            0.75
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 0.170000762, 0.170000762, 0.170000762, 0.39000535 }
                        }
                    }
                }
                pass: i16 = -200
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 80
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.400000006
                                0.5
                            }
                            values: list[f32] = {
                                1.5
                                0
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.200000003
                    erosionMapName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_1Q_SmokeErode.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0.0200045779, 0 }
                    }
                }
                depthBiasFactors: vec2 = { 0, 5 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin17/Particles/Chogath_Skin17_Recall_green_TX_CM.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                lifetime: option[f32] = {
                    8
                }
                isSingleParticle: flag = true
                emitterName: string = "Center_ALpha20"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 30, -2 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.skl"
                        mAnimationName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_B.anm"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.670000017
                            0.699999988
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 220
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 80
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.600000024
                                0.670000017
                            }
                            values: list[f32] = {
                                1
                                0
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0
                    erosionMapName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_yan_9.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_yan_6.tex"
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = -0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Center_ALpha21"
                importance: u8 = 2
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 10, 30, 5 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.skl"
                        mAnimationName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.anm"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.400000006
                            0.479999989
                            0.5
                            0.560000002
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.730006874 }
                            { 1, 1, 1, 0.340001523 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 130
                }
                depthBiasFactors: vec2 = { 0, 5 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin17/Particles/Chogath_Skin17_Recall_green_TX_CM.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                lifetime: option[f32] = {
                    8
                }
                isSingleParticle: flag = true
                emitterName: string = "Center_ALpha22"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 30, -2 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.skl"
                        mAnimationName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_B.anm"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.579995394 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.100000001
                            0.200000003
                            0.400000006
                            0.75
                        }
                        values: list[vec4] = {
                            { 1, 0, 0, 0 }
                            { 1, 0, 0, 1 }
                            { 1, 0, 0, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 190
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 80
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.600000024
                                0.670000017
                            }
                            values: list[f32] = {
                                0.850000024
                                0
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_yan_9.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_colorhold.tex"
                texAddressModeBase: u8 = 2
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = -0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Center_ALpha23"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 30, -3 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.skl"
                        mAnimationName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.anm"
                    }
                }
                blendMode: u8 = 1
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.159999996
                            0.230000004
                            0.600000024
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 220
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 80
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.600000024
                                0.670000017
                            }
                            values: list[f32] = {
                                1
                                0
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_yan_9.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0.0200045779, 0 }
                    }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_yan_6.tex"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = -0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 6
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Center_ALpha24"
                importance: u8 = 2
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 10, 30, 5 }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.skl"
                        mAnimationName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.anm"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.674509823, 0.298039228, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.25
                            0.349999994
                            0.699999988
                            0.730000019
                            0.899999976
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 120
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 80
                }
                depthBiasFactors: vec2 = { 0, 5 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_yan_3220.tex"
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = -0.5
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Center_ALpha25"
                importance: u8 = 2
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 30, -2 }
                }
                FlexShapeDefinition: pointer = VfxFlexShapeDefinitionData {
                    scaleBirthScaleByBoundObjectSize: f32 = 0.00499999989
                }
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mMeshName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.skn"
                        mMeshSkeletonName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.skl"
                        mAnimationName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_skin14_Recall_SHAN_SH_A_WIPq.anm"
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0, 0, 0.500007629 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.159999996
                            0.300000012
                            0.5
                            0.800000012
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.170000762 }
                        }
                    }
                }
                pass: i16 = 150
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 80
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.460000008
                                0.550000012
                            }
                            values: list[f32] = {
                                1
                                0
                            }
                        }
                    }
                    erosionFeatherOut: f32 = 0.400000006
                    erosionMapName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_yan_9.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0.0200045779, 0 }
                    }
                }
                depthBiasFactors: vec2 = { 0, 5 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_yan_6.tex"
            }
        }
        visibilityRadius: f32 = 18000
        particleName: string = "Chogath_Skin17_Recall_MountainMat_danshan"
        particlePath: string = "Characters/Chogath/Skins/Skin17/Particles/Chogath_Skin17_Recall_MountainMat_danshan"
        overrideScaleCap: option[f32] = {
            200
        }
    }
    "Characters/Chogath/Skins/Skin17/Particles/Chogath_Skin17_W_cas" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_W_cas_child"
                        }
                    }
                }
                emitterName: string = "Parent Particle"
                particleIsLocalOrientation: flag = true
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_W_cas_child_1"
                        }
                    }
                }
                emitterName: string = "Parent Particle1"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 0, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_W_cas_child_2"
                        }
                    }
                }
                emitterName: string = "Parent Particle2"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, 15, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_W_cas_child_2"
                        }
                    }
                }
                emitterName: string = "Parent Particle3"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 180, -15, 0 }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_W_cas_child_3"
                        }
                    }
                }
                emitterName: string = "Parent Particle4"
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 50, 20, 150 }
                }
                particleIsLocalOrientation: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, -15, 0 }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = -0.400000006
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.699999988
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Kayn_Assassin_Fresnel6"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { -0.00999999978, 0, -0.00999999978 }
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.600000024 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.764705896, 0.431372553, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.400000006
                        }
                        values: list[vec4] = {
                            { 1, 0.764705896, 0.431372553, 1 }
                            { 1, 0.764705896, 0.431372553, 1 }
                            { 1, 0, 0, 1 }
                        }
                    }
                }
                pass: i16 = 180
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.100000001
                                0.5
                            }
                            values: list[f32] = {
                                0
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_1Q_SmokeErode.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0.0200045779, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -6 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_2022.tex"
                materialOverrideDefinitions: list[embed] = {
                    VfxMaterialOverrideDefinitionData {
                        subMeshName: option[string] = {
                            "Body"
                        }
                        material: link = "Characters/Chogath/Skins/Skin17/Materials/ChoGath_Skin17_FlowMap_Bloom_inst"
                    }
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
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Kayn_Assassin_Fresnel7"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { -0.00999999978, 0, -0.00999999978 }
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
                    constantValue: vec4 = { 1, 1, 1, 0.60999465 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.937254906, 0.145098045, 0.0431372561, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            1
                        }
                        values: list[vec4] = {
                            { 0.937254906, 0.145098045, 0.0431372561, 0 }
                            { 0.937254906, 0.145098045, 0.0431372561, 1 }
                            { 0.937254906, 0.145098045, 0.0431372561, 0 }
                        }
                    }
                }
                pass: i16 = 100
                depthBiasFactors: vec2 = { -1, -6 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_1995.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_E_luoxuan_040.tex"
                    ParticleIntegratedUvScrollMult: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0, 0.200000003 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0, 0.200000003 }
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
                    constantValue: f32 = 2
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Kayn_Assassin_Fresnel8"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { -0.00999999978, 0, -0.00999999978 }
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
                    constantValue: vec4 = { 1, 1, 1, 0.800000012 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.592156887, 0, 0, 0.819607854 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                        }
                        values: list[vec4] = {
                            { 0.592156887, 0, 0, 0 }
                            { 0.592156887, 0, 0, 0.819607854 }
                            { 0.592156887, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 150
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_1996.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_E_luoxuan_040.tex"
                    ParticleIntegratedUvScrollMult: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0.5, 0 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.5, 0 }
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
                    constantValue: f32 = 2
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Kayn_Assassin_Fresnel9"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { -0.00999999978, 0, -0.00999999978 }
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
                    constantValue: vec4 = { 1, 0, 0, 0.819607854 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.800000012
                        }
                        values: list[vec4] = {
                            { 1, 0, 0, 0 }
                            { 1, 0, 0, 0.819607854 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 180
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {}
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_1996.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_E_luoxuan_040.tex"
                    ParticleIntegratedUvScrollMult: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0.5, 0 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.5, 0 }
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
                    constantValue: f32 = 2.5
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Kayn_Assassin_Fresnel10"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { -0.00999999978, 0, -0.00999999978 }
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
                    constantValue: vec4 = { 1, 0.200000003, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.200000003, 0, 0 }
                            { 1, 0.200000003, 0, 1 }
                            { 1, 0.200000003, 0, 0 }
                        }
                    }
                }
                pass: i16 = 180
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_1994.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2.5
                }
                lifetime: option[f32] = {
                    5
                }
                isSingleParticle: flag = true
                emitterName: string = "Kayn_Assassin_Fresnel11"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { -0.00999999978, 0, -0.00999999978 }
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
                    constantValue: vec4 = { 1, 0, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0, 0, 0 }
                            { 1, 0, 0, 1 }
                            { 1, 0, 0, 0 }
                        }
                    }
                }
                pass: i16 = 180
                depthBiasFactors: vec2 = { -1, -2 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_1994.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_E_luoxuan_040.tex"
                    ParticleIntegratedUvScrollMult: embed = IntegratedValueVector2 {
                        constantValue: vec2 = { 0.5, 0 }
                        dynamics: pointer = VfxAnimatedVector2fVariableData {
                            times: list[f32] = {
                                0
                            }
                            values: list[vec2] = {
                                { 0.5, 0 }
                            }
                        }
                    }
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.550000012
                }
                particleLinger: option[f32] = {
                    10.5500002
                }
                lifetime: option[f32] = {
                    0.25
                }
                emitterName: string = "StrokeDissolve6"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 2500 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 1, 2 }
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 100, 150 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.58431375 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.00171526591
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.58431375 }
                            { 1, 1, 1, 0.58431375 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.25
                            0.400000006
                        }
                        values: list[vec4] = {
                            { 1, 0.674509823, 0.145098045, 1 }
                            { 1, 0.164705887, 0, 1 }
                            { 0.86999315, 0, 0, 0.659998477 }
                            { 0.100007631, 0.0800030529, 0.149996191, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 1.39999998
                    erosionMapName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_W_Erosion_01.tex"
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            { 0, 0, 360 }
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
                                    0.5
                                    0.50999999
                                    1
                                }
                                keyValues: list[f32] = {
                                    -200
                                    -100
                                    100
                                    200
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 22, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.991423666
                        }
                        values: list[vec3] = {
                            { 3, 0.5, 0.5 }
                            { 40, 2.44758081, 2.44758081 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_W_ju11n_yunu.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    10.5500002
                }
                lifetime: option[f32] = {
                    0.25
                }
                emitterName: string = "StrokeDissolve7"
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 100, 150 }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.58431375 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0.00171526591
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.58431375 }
                            { 1, 1, 1, 0.58431375 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.25
                            0.400000006
                        }
                        values: list[vec4] = {
                            { 1, 0.674509823, 0.145098045, 1 }
                            { 1, 0.164705887, 0, 1 }
                            { 0.86999315, 0, 0, 0.659998477 }
                            { 0.100007631, 0.0800030529, 0.149996191, 0 }
                        }
                    }
                }
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionFeatherIn: f32 = 0.400000006
                    erosionFeatherOut: f32 = 0.400000006
                    erosionSliceWidth: f32 = 1.39999998
                    erosionMapName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_W_Erosion_01.tex"
                    erosionMapAddressMode: u8 = 0
                }
                disableBackfaceCull: bool = true
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0, 360 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        probabilityTables: list[pointer] = {
                            VfxProbabilityTableData {}
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
                            { 0, 0, 360 }
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
                                    0.5
                                    0.50999999
                                    1
                                }
                                keyValues: list[f32] = {
                                    -200
                                    -100
                                    100
                                    200
                                }
                            }
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                            { 0, 0, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 10, 1, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.991423666
                        }
                        values: list[vec3] = {
                            { 3, 0.5, 0.5 }
                            { 40, 2.44758081, 2.44758081 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_W_ju11n_yunu.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLinger: option[f32] = {
                    11
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Chogath_W_cas_child"
                        }
                    }
                }
                emitterName: string = "Parent Particle5"
                disabled: bool = true
                particleIsLocalOrientation: flag = true
            }
        }
        particleName: string = "Chogath_Skin17_W_cas"
        particlePath: string = "Characters/Chogath/Skins/Skin17/Particles/Chogath_Skin17_W_cas"
    }
    "Characters/Chogath/Skins/Skin17/Particles/Chogath_Skin17_Idle_clould3" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 4
                }
                particleLinger: option[f32] = {
                    3
                }
                emitterName: string = "Avatar13"
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "Tail"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.0117647061, 0.53725493, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.699999988
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
                pass: i16 = 50
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 0.800000012
                    }
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_E_luoxuan_040.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -20 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                texture: string = "ASSETS/Characters/Chogath/skins/Skin17/Particles/Chogath_Skin17_E_juan_yun182.tex"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 0.300000012 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.300000012 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { -1, -1 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_Idle_jianbian_837.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    3
                }
                lifetime: option[f32] = {
                    0.100000001
                }
                isSingleParticle: flag = true
                emitterName: string = "Avatar14"
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
                    constantValue: vec4 = { 0.00392156886, 0.53725493, 1, 1 }
                }
                pass: i16 = 50
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 0.800000012
                    }
                    erosionFeatherOut: f32 = 0.5
                    erosionMapName: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_E_luoxuan_040.tex"
                    erosionMapChannelMixer: embed = ValueColor {
                        constantValue: vec4 = { 1, 0, 0, 0 }
                    }
                }
                depthBiasFactors: vec2 = { -1, -20 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_W_mult.tex"
                particleUVScrollRate: embed = IntegratedValueVector2 {
                    constantValue: vec2 = { 0, 0.100000001 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.100000001 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 5, -2 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_Q_jianbian_211.tex"
                }
            }
        }
        visibilityRadius: f32 = 5000
        particleName: string = "Chogath_Skin17_Idle_clould3"
        particlePath: string = "Characters/Chogath/Skins/Skin17/Particles/Chogath_Skin17_Idle_clould3"
        flags: u16 = 198
    }
}
