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
    "Characters/Yasuo/Skins/Skin38" = SkinCharacterDataProperties {
        skinClassification: u32 = 2
        championSkinName: string = "YasuoSkin38"
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
    "Characters/Yasuo/Skins/Skin38/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Yasuo_BA_Crit_hit_01" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_BA_Crit_hit_01"
            "Yasuo_BA_Crit_hit_02" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_BA_Crit_hit_02"
            "Yasuo_BA_Crit_hit_03" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_BA_Crit_hit_03"
            "Yasuo_BA_Crit_hit_04" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_BA_Crit_hit_04"
            "Yasuo_BA_hit_tar_01" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_BA_hit_tar_01"
            "Yasuo_BA_hit_tar_02" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_BA_hit_tar_02"
            "Yasuo_BA_hit_tar_03" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_BA_hit_tar_03"
            "Yasuo_BA_hit_tar_04" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_BA_hit_tar_04"
            "Yasuo_BA_trail_1" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_BA_trail_1"
            "Yasuo_BA_trail_2" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_BA_trail_2"
            "Yasuo_BA_trail_3" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_BA_trail_3"
            "Yasuo_BA_trail_4" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_BA_trail_4"
            "Yasuo_Dance_flute_wind" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Dance_flute_wind"
            "Yasuo_deathscaress_buf" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_deathscaress_buf"
            "Yasuo_Emote_dance_in_sound" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Emote_dance_in_sound"
            "Yasuo_Emote_dance_sound" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Emote_dance_sound"
            "Yasuo_Emote_death_sound" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Emote_death_sound"
            "Yasuo_Emote_joke_sound" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Emote_joke_sound"
            "Yasuo_Emote_laugh_sound" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Emote_laugh_sound"
            "Yasuo_Emote_taunt2_sound" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Emote_taunt2_sound"
            "Yasuo_Emote_taunt_generic" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Emote_taunt_generic"
            "Yasuo_Emote_taunt_interactive_ninja" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Emote_taunt_interactive_ninja"
            "Yasuo_Emote_taunt_interactive_riven" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Emote_taunt_interactive_riven"
            "Yasuo_Emote_taunt_interactive_yi" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Emote_taunt_interactive_yi"
            "Yasuo_Emote_taunt_sound" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Emote_taunt_sound"
            "Yasuo_EQ3_cas" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_EQ3_cas"
            "Yasuo_EQ_cas" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_EQ_cas"
            "Yasuo_EQ_SwordGlow" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_EQ_SwordGlow"
            "Yasuo_E_Dash" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_E_Dash"
            "Yasuo_E_dash_hit" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_E_dash_hit"
            "Yasuo_E_timer1" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_E_timer1"
            "Yasuo_E_timer2" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_E_timer2"
            "Yasuo_E_timer3" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_E_timer3"
            "Yasuo_E_timer4" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_E_timer4"
            "Yasuo_E_timer5" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_E_timer5"
            "Yasuo_I_sheath_spark" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_I_sheath_spark"
            "Yasuo_NightmareBot_E_timer1" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_E_timer1"
            "Yasuo_NightmareBot_E_timer2" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_E_timer2"
            "Yasuo_NightmareBot_E_timer3" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_E_timer3"
            "Yasuo_NightmareBot_E_timer4" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_E_timer4"
            "Yasuo_NightmareBot_E_timer5" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_E_timer5"
            "Yasuo_Passive_Activate" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_passive_activate"
            "Yasuo_Passive_Burst" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Passive_Burst"
            "Yasuo_Q3_Hand" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Q3_Hand"
            "Yasuo_Q3_Indicator_Ring" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Q3_Indicator_Ring"
            "Yasuo_Q3_Indicator_Ring_alt" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Q3_Indicator_Ring_alt"
            "Yasuo_Q_Hand" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Q_Hand"
            "Yasuo_Q_hit_tar" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Q_hit_tar"
            "Yasuo_Q_sound" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Q_sound"
            "Yasuo_Q_WindStrike" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Q_WindStrike"
            "Yasuo_Q_WindStrike_02" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Q_windstrike_02"
            "Yasuo_Q_wind_hit_tar" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Q_wind_hit_tar"
            "Yasuo_Q_wind_mis" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Q_wind_mis"
            "Yasuo_Q_wind_ready_buff" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Q_wind_ready_buff"
            0xc542e434 = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Recall"
            "Yasuo_recall_start_sound" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_recall_start_sound"
            "Yasuo_R_cantcast_beam" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_R_cantcast_beam"
            "Yasuo_R_cas_marker_01" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_R_cas_marker_01"
            "Yasuo_R_CloneVFX" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_R_CloneVFX"
            "Yasuo_R_dash" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_R_dash"
            "Yasuo_R_impact_tar" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_R_impact_tar"
            "Yasuo_R_indicator_beam" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_R_indicator_beam"
            "Yasuo_R_land_tar" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_R_land_tar"
            "Yasuo_R_slash_cas" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_R_slash_cas"
            "Yasuo_R_SwordGlow" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_R_SwordGlow"
            "Yasuo_R_tar_imp_01" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_R_tar_imp_01"
            "Yasuo_R_tar_marker_01" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_R_tar_marker_01"
            "Yasuo_R_tar_marker_02" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_R_tar_marker_02"
            "Yasuo_Taunt_spit" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Taunt_spit"
            "Yasuo_Wall_XinZhao_OLD" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Wall_XinZhao_OLD"
            "Yasuo_W_windwall1" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_W_windwall1"
            "Yasuo_W_windwall2" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_W_windwall2"
            "Yasuo_W_windwall3" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_W_windwall3"
            "Yasuo_W_windwall4" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_W_windwall4"
            "Yasuo_W_windwall5" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_W_windwall5"
            "Yasuo_W_windwall_activate" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_W_windwall_activate"
            "Yasuo_W_Windwall_big_impact" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_W_windwall_big_impact"
            "Yasuo_W_windwall_enemy_01" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_w_windwall_enemy_01"
            "Yasuo_W_windwall_enemy_02" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_w_windwall_enemy_02"
            "Yasuo_W_windwall_enemy_03" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_w_windwall_enemy_03"
            "Yasuo_W_windwall_enemy_04" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_w_windwall_enemy_04"
            "Yasuo_W_windwall_enemy_05" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_w_windwall_enemy_05"
            "Yasuo_Q_Odyssey_Wandering_wind_mis" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Q_wind_mis"
            "Yasuo_Q_Odyssey_Growing_wind_mis" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Q_wind_mis"
            "Yasuo_Q_Odyssey_Wandering_Growing_wind_mis" = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Q_wind_mis"
            0x79b5e280 = "Characters/Yasuo/Skins/Skin38/Particles/Yasuo_Skin38_Z_Idle_ShoulderGlow"
            0x87eb6a8f = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Z_Recall_Pond"
            0x9c76d187 = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Z_Recall_TreeBaseRipple"
            0x86e8ad4f = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Z_Recall_FootRipples"
            0xd2537e8a = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Z_Recall_FlowerRipples"
            0x3dd62ddb = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Z_Recall_StandingRipples"
            0xd368cb74 = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Z_Recall_SwordSwipe1"
            0xd668d02d = "Characters/Yasuo/Skins/Skin36/Particles/Yasuo_Skin36_Z_Recall_SwordSwipe2"
        }
    }
    "Characters/Yasuo/Skins/Skin38/Particles/Yasuo_Skin38_Z_Idle_ShoulderGlow" = VfxSystemDefinitionData {
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
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Yasuo/Skins/Skin38/Particles/Yasuo_Skin38_TX_ArmMask.dds"
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
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Yasuo/Skins/Skin38/Particles/Yasuo_Skin38_TX_ArmMask.dds"
                }
            }
        }
        particleName: string = "Yasuo_Skin38_Z_Idle_ShoulderGlow"
        particlePath: string = "Characters/Yasuo/Skins/Skin38/Particles/Yasuo_Skin38_Z_Idle_ShoulderGlow"
    }
}
