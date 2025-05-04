#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Chogath_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin5_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Characters/Chogath/Chogath.bin"
    "DATA/Chogath_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
    "DATA/Characters/Chogath/Animations/Skin0.bin"
    "DATA/Chogath_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin2_Skins_Skin3_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin8_Skins_Skin9.bin"
}
entries: map[hash,embed] = {
    "Characters/Chogath/Skins/Skin9" = SkinCharacterDataProperties {
        skinClassification: u32 = 2
        championSkinName: string = "ChogathSkin09"
        skinParent: i32 = 5
        metaDataTags: string = "faction:void,gender:male,race:monster,skinline:battlecast"
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Characters/Chogath/skins/skin05/ChogathLoadScreen_5.tex"
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
    "Characters/Chogath/Skins/Skin9/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Chogath_BA_tar" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_BA_tar"
            "Chogath_Death_SoundDust" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_Death_SoundDust"
            "Chogath_E_Cas" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_E_Cas"
            "Chogath_E_mis" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_E_mis"
            "Chogath_E_mis2" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_E_mis"
            "Chogath_E_mis3" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_E_mis"
            "Chogath_E_mis4" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_E_mis"
            "Chogath_E_mis5" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_E_mis"
            "Chogath_E_mis6" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_E_mis"
            "Chogath_E_tar" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_tar"
            "Chogath_E_Tar02" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_E_Tar02"
            "Chogath_P_heal" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_P_heal"
            "Chogath_Q_Ally_team" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_Q_Ally_team"
            "Chogath_Q_cas" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_Q_cas"
            "Chogath_Q_Enemy_team" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_Q_Enemy_team"
            "Chogath_R_indicator" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_R_indicator"
            "Chogath_R_tar" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_R_tar"
            "Chogath_W_cas" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_W_cas"
            "Chogath_W_Sound01" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_W_Sound01"
            "Chogath_W_tar" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_W_tar"
            "Chogath_E_Cas_Spikes" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_E_Cas_Spikes"
            "Chogath_E_mis_child" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_E_mis_child"
            "Chogath_W_cas_child" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_W_cas_child"
            "Chogath_R_mis" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_R_mis"
            "Chogath_BA_Crit_tar" = "Characters/Chogath/Skins/Skin0/Particles/Chogath_Base_BA_Crit_tar"
            "Chogath_audio_level11" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_audio_level11"
            "Chogath_audio_level15" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_audio_level15"
            "Chogath_audio_level18" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_audio_level18"
            "Chogath_audio_level6" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_audio_level6"
            "Chogath_audio_revive" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_audio_revive"
            "Chogath_beam_end_sound" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_beam_end_sound"
            "Chogath_beam_start_sound" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_beam_start_sound"
            "Chogath_DeathXP" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_DeathXP"
            "Chogath_emote_death_sound" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_emote_death_sound"
            "Chogath_emote_joke_sound" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_emote_joke_sound"
            "Chogath_Joke_SmokeL" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_Joke_SmokeL"
            "Chogath_Joke_SmokeR" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_Joke_SmokeR"
            "Chogath_Joke_SoundL" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_Joke_SoundL"
            "Chogath_Joke_SoundR" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_Joke_SoundR"
            "Chogath_Q_Dirt" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_Q_Dirt"
            "Chogath_R_audio_01" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_R_audio_01"
            "Chogath_R_audio_03" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_R_audio_03"
            "Chogath_R_audio_06" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_R_audio_06"
            "Chogath_R_Glow_Eye_L" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_R_Glow_Eye_L"
            "Chogath_R_Glow_Eye_R" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_R_Glow_Eye_R"
            "Chogath_R_Glow_Red01" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_R_Glow_Red01"
            "Chogath_R_textureswap" = "Characters/Chogath/Skins/Skin9/Particles/Chogath_Skin09_R_textureswap"
            "Chogath_SpeakersL_cas" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_SpeakersL_cas"
            "Chogath_SpeakersR_cas" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_SpeakersR_cas"
            "Chogath_Vorpal_Cas" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_Vorpal_Cas"
            "Chogath_Z_dance_sound" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_Z_dance_sound"
            "Chogath_Skin05_E_mis_child" = "Characters/Chogath/Skins/Skin5/Particles/Chogath_Skin05_E_mis_child"
        }
    }
    "Characters/Chogath/Skins/Skin9/Particles/Chogath_Skin09_R_textureswap" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.0500000007
                }
                particleLinger: option[f32] = {
                    10
                }
                isSingleParticle: flag = true
                emitterName: string = "base"
                importance: u8 = 2
                particleColorTexture: string = "ASSETS/Characters/Chogath/skins/skin05/Particles/Chogath_Skin05_R_color-hold.tex"
                meshRenderFlags: u8 = 0
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Chogath/skins/skin05/Particles/Chogath_Skin05_R_missing_instant.tex"
                materialOverrideDefinitions: list[embed] = {
                    VfxMaterialOverrideDefinitionData {
                        subMeshName: option[string] = {
                            "chogath_battlecast_MD_blinn3"
                        }
                        overrideBlendMode: u32 = 2
                        baseTexture: string = "ASSETS/Characters/Chogath/skins/Skin09/Particles/Chogath_Skin09_textureswap.tex"
                    }
                }
            }
        }
        particleName: string = "Chogath_Skin09_R_textureswap"
        particlePath: string = "Characters/Chogath/Skins/Skin9/Particles/Chogath_Skin09_R_textureswap"
    }
}
