#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Yasuo/Yasuo.bin"
    "DATA/Characters/Yasuo/Animations/Skin0.bin"
    "DATA/Yasuo_Skins_Skin68_Skins_Skin69_Skins_Skin70_Skins_Skin71_Skins_Skin72_Skins_Skin73_Skins_Skin74_Skins_Skin75_Skins_Skin76.bin"
    "DATA/Yasuo_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin33_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin4_Skins_Skin40_Skins_Skin41_Skins_Skin42_Skins_Skin43_Skins_Skin44_Skins_Skin45_Skins_Skin46_Skins_Skin47_Skins_Skin48_Skins_Skin49_Skins_Skin5_Skins_Skin50_Skins_Skin51_Skins_Skin52_Skins_Skin53_Skins_Skin56_Skins_Skin57_Skins_Skin58_Skins_Skin59_Skins_Skin6_Skins_Skin60_Skins_Skin61_Skins_Skin62_Skins_Skin63_Skins_Skin64_Skins_Skin65_Skins_Skin66_Skins_Skin67_Skins_Skin68_Skins_Skin69_Skins_Skin7_Skins_Skin70_Skins_Skin71_Skins_Skin72_Skins_Skin73_Skins_Skin74_Skins_Skin75_Skins_Skin76_Skins_Skin77_Skins_Skin78_Skins_Skin79_Skins_Skin8_Skins_Skin80_Skins_Skin81_Skins_Skin82_Skins_Skin83_Skins_Skin84_Skins_Skin85_Skins_Skin86.bin"
}
entries: map[hash,embed] = {
    "Characters/Yasuo/Skins/Skin72" = SkinCharacterDataProperties {
        skinClassification: u32 = 2
        championSkinName: string = "YasuoSkin72"
        skinParent: i32 = 68
        metaDataTags: string = "gender:male,faction:ionia,race:human,element:wind,skinline:otherroads"
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Characters/Yasuo/Skins/Skin68/YasuoLoadScreen_68.tex"
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
    "Characters/Yasuo/Skins/Skin72/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Yasuo_BA_Crit_hit_01" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_BA_Crit_hit_01"
            "Yasuo_BA_Crit_hit_02" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_BA_Crit_hit_02"
            "Yasuo_BA_Crit_hit_03" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_BA_Crit_hit_03"
            "Yasuo_BA_Crit_hit_04" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_BA_Crit_hit_04"
            "Yasuo_BA_hit_tar_01" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_BA_hit_tar_01"
            "Yasuo_BA_hit_tar_02" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_BA_hit_tar_02"
            "Yasuo_BA_hit_tar_03" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_BA_hit_tar_03"
            "Yasuo_BA_hit_tar_04" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_BA_hit_tar_04"
            "Yasuo_BA_trail_1" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_BA_trail_1"
            "Yasuo_BA_trail_2" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_BA_trail_2"
            "Yasuo_BA_trail_3" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_BA_trail_3"
            "Yasuo_BA_trail_4" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_BA_trail_4"
            "Yasuo_Dance_flute_wind" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Dance_flute_wind"
            "Yasuo_deathscaress_buf" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_deathscaress_buf"
            "Yasuo_Emote_dance_in_sound" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Emote_dance_in_sound"
            "Yasuo_Emote_dance_sound" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Emote_dance_sound"
            "Yasuo_Emote_death_sound" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Emote_death_sound"
            "Yasuo_Emote_joke_sound" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Emote_joke_sound"
            "Yasuo_Emote_laugh_sound" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Emote_laugh_sound"
            "Yasuo_Emote_taunt2_sound" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Emote_taunt2_sound"
            "Yasuo_Emote_taunt_generic" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Emote_taunt_generic"
            "Yasuo_Emote_taunt_interactive_ninja" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Emote_taunt_interactive_ninja"
            "Yasuo_Emote_taunt_interactive_riven" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Emote_taunt_interactive_riven"
            "Yasuo_Emote_taunt_interactive_yi" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Emote_taunt_interactive_yi"
            "Yasuo_Emote_taunt_sound" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Emote_taunt_sound"
            "Yasuo_EQ3_cas" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_EQ3_cas"
            "Yasuo_EQ_cas" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_EQ_cas"
            "Yasuo_EQ_SwordGlow" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_EQ_SwordGlow"
            "Yasuo_E_Dash" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_E_Dash"
            "Yasuo_E_dash_hit" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_E_dash_hit"
            "Yasuo_E_timer1" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_E_timer1"
            "Yasuo_E_timer2" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_E_timer2"
            "Yasuo_E_timer3" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_E_timer3"
            "Yasuo_E_timer4" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_E_timer4"
            "Yasuo_E_timer5" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_E_timer5"
            "Yasuo_I_sheath_spark" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_I_sheath_spark"
            "Yasuo_NightmareBot_E_timer1" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_E_timer1"
            "Yasuo_NightmareBot_E_timer2" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_E_timer2"
            "Yasuo_NightmareBot_E_timer3" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_E_timer3"
            "Yasuo_NightmareBot_E_timer4" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_E_timer4"
            "Yasuo_NightmareBot_E_timer5" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_E_timer5"
            "Yasuo_Passive_Activate" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_passive_activate"
            "Yasuo_Passive_Burst" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Passive_Burst"
            "Yasuo_Q3_Hand" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q3_Hand"
            "Yasuo_Q3_Indicator_Ring" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q3_Indicator_Ring"
            "Yasuo_Q3_Indicator_Ring_alt" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q3_Indicator_Ring_alt"
            "Yasuo_Q_Hand" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q_Hand"
            "Yasuo_Q_hit_tar" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q_hit_tar"
            "Yasuo_Q_sound" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q_sound"
            "Yasuo_Q_WindStrike" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q_WindStrike"
            "Yasuo_Q_WindStrike_02" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q_windstrike_02"
            "Yasuo_Q_wind_hit_tar" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q_wind_hit_tar"
            "Yasuo_Q_wind_mis" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q_wind_mis"
            "Yasuo_Q_wind_ready_buff" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q_wind_ready_buff"
            0xc542e434 = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Recall"
            "Yasuo_recall_start_sound" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_recall_start_sound"
            "Yasuo_R_cantcast_beam" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_R_cantcast_beam"
            "Yasuo_R_cas_marker_01" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_R_cas_marker_01"
            "Yasuo_R_CloneVFX" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_R_CloneVFX"
            "Yasuo_R_dash" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_R_dash"
            "Yasuo_R_impact_tar" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_R_impact_tar"
            "Yasuo_R_indicator_beam" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_R_indicator_beam"
            "Yasuo_R_land_tar" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_R_land_tar"
            "Yasuo_R_slash_cas" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_R_slash_cas"
            "Yasuo_R_SwordGlow" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_R_SwordGlow"
            "Yasuo_R_tar_imp_01" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_R_tar_imp_01"
            "Yasuo_R_tar_marker_01" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_R_tar_marker_01"
            "Yasuo_R_tar_marker_02" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_R_tar_marker_02"
            "Yasuo_Taunt_spit" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Taunt_spit"
            "Yasuo_Wall_XinZhao_OLD" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Wall_XinZhao_OLD"
            "Yasuo_W_windwall1" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_W_windwall1"
            "Yasuo_W_windwall2" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_W_windwall2"
            "Yasuo_W_windwall3" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_W_windwall3"
            "Yasuo_W_windwall4" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_W_windwall4"
            "Yasuo_W_windwall5" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_W_windwall5"
            "Yasuo_W_windwall_activate" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_W_windwall_activate"
            "Yasuo_W_Windwall_big_impact" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_W_windwall_big_impact"
            "Yasuo_W_windwall_enemy_01" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_w_windwall_enemy_01"
            "Yasuo_W_windwall_enemy_02" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_w_windwall_enemy_02"
            "Yasuo_W_windwall_enemy_03" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_w_windwall_enemy_03"
            "Yasuo_W_windwall_enemy_04" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_w_windwall_enemy_04"
            "Yasuo_W_windwall_enemy_05" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_w_windwall_enemy_05"
            "Yasuo_Q_Odyssey_Wandering_wind_mis" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q_wind_mis"
            "Yasuo_Q_Odyssey_Growing_wind_mis" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q_wind_mis"
            "Yasuo_Q_Odyssey_Wandering_Growing_wind_mis" = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q_wind_mis"
            0xb104e64a = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_swipe_one_sand"
            0xf76bb923 = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_wind_trail"
            0x774236ee = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_arraow"
            0xc42678ca = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_Arrow_Impact"
            0xc3e98dfa = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_Kindred_Wolf_Soul"
            0xe7eea1f5 = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_Kindred_Wolf_Soul_Start"
            0xdd2d7072 = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_Wolf_Fly_Through_Yasuo"
            0x0067c204 = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_Ground_Wind"
            0x634b3137 = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_Arms_Power"
            0x3845978d = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_Yasuo_Soul"
            0xe43c6e60 = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_Swipe"
            0x91d127cd = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_Swipe_2"
            0x973b5b2c = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_Kindred_Wolf_Soul_End"
            0xf83913a6 = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_Window"
            0x90d1263a = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_Swipe_3"
            0x15367f75 = "Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Z_Yasuo_Sword_End"
            0x97f876a5 = "Characters/Yasuo/Skins/Skin72/Particles/Yasuo_Skin72_Idle_Arms_Glow"
        }
    }
    "Characters/Yasuo/Skins/Skin72/Materials/Arms_Glow_inst" = StaticMaterialDef {
        name: string = "Characters/Yasuo/Skins/Skin72/Materials/Arms_Glow_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "AlphaMask_Fresnel"
                texturePath: string = "ASSETS/Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Idle_Mask_02.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Diffuse_Texture"
                texturePath: string = "ASSETS/Characters/Yasuo/Skins/Skin72/Yasuo_Skin72_TX_CM.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Scroll_01"
                texturePath: string = "ASSETS/Characters/LeeSin/Skins/Skin31/Particles/LeeSin_Skin31_E_Bottom_02.tex"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Mask"
                texturePath: string = "ASSETS/Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Idle_Mask_02.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Scroll_02"
                texturePath: string = "ASSETS/Characters/Varus/Skins/Skin44/Particles/Varus_Skin34_Cape_Nebula.dds"
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Scroll_03"
                texturePath: string = "ASSETS/Characters/LeeSin/Skins/Skin31/Particles/LeeSin_Skin31_E_Bottom_02.tex"
                addressW: u32 = 1
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Size"
                value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Alpha_Bias"
            }
            StaticMaterialShaderParamDef {
                name: string = "Texture_UV_Scale01"
            }
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Color"
                value: vec4 = { 0.137254909, 0.611764729, 0.862745106, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Panning_Noise_Color"
                value: vec4 = { 0.109803922, 0.203921571, 0.305882365, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollTexture_Control01"
            }
            StaticMaterialShaderParamDef {
                name: string = "Texture_UV_Scale02"
                value: vec4 = { 8, 5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollTexture_Control02"
                value: vec4 = { 0, 0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Texture_UV_Scale03"
            }
            StaticMaterialShaderParamDef {
                name: string = "ScrollTexture_Control03"
            }
            StaticMaterialShaderParamDef {
                name: string = "BloomIntensity"
                value: vec4 = { 2, 0, 0, 0 }
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "INVERT_FRESNEL"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_DIFFUSE_ALPHA"
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
                        shader: link = "Shaders/SkinnedMesh/MultiMask_Panner_Fresnel"
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
    "Characters/Yasuo/Skins/Skin72/Materials/Hair_Bloom_inst" = StaticMaterialDef {
        name: string = "Characters/Yasuo/Skins/Skin72/Materials/Hair_Bloom_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "Diffuse_Texture"
                texturePath: string = "ASSETS/Characters/Yasuo/Skins/Skin72/Yasuo_Skin72_TX_CM.dds"
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Mask_Texture"
                texturePath: string = "ASSETS/Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Idle_Mask.dds"
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Additive_Intensity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Noise_Scale"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Scroll_Speed"
            }
            StaticMaterialShaderParamDef {
                name: string = "Addative_Color"
                value: vec4 = { 0.109803922, 0.203921571, 0.305882365, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_color"
                value: vec4 = { 0.137254909, 0.611764729, 0.862745106, 1 }
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "OVERLAY_ADDATIVE"
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
                        shader: link = "Shaders/SkinnedMesh/ScrollingUVs_Simple"
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
    "Characters/Yasuo/Skins/Skin72/Particles/Yasuo_Skin72_Idle_Arms_Glow" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 10
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
                particleLinger: option[f32] = {
                    11
                }
                emitterName: string = "wind"
                importance: u8 = 2
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
                    constantValue: f32 = 0.899999976
                }
                SpawnShape: pointer = VfxShapeSphere {
                    flags: u8 = 1
                    radius: f32 = 8
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 0 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.105714507, 0.549019635, 0.0904249623, 0.301960796 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.408457726
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.144243538, 0.73232621, 0.778072774, 0 }
                        }
                    }
                }
                pass: i16 = 100
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
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
                            { 0, 100, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 1.70000005, 1.70000005, 1.70000005 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Idle_wind_wispy_alpha_fix.dds"
                numFrames: u16 = 16
                texDiv: vec2 = { 4, 4 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                isSingleParticle: flag = true
                emitterName: string = "LargeGlow_Shoulder"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.149996191 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.62999922 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.150000006
                            0.449999988
                            1
                        }
                        values: list[vec4] = {
                            { 0.137254909, 0.862745106, 0.172549024, 0.62999922 }
                            { 0.137254909, 0.862745106, 0.172549024, 0.195176229 }
                            { 0.137254909, 0.862745106, 0.172549024, 0.284117311 }
                            { 0.109803922, 0.478431374, 0.190844581, 0 }
                        }
                    }
                }
                pass: i16 = 200
                colorLookUpTypeY: u8 = 3
                alphaRef: u8 = 0
                softParticleParams: pointer = VfxSoftParticleDefinitionData {
                    deltaIn: f32 = 30
                }
                depthBiasFactors: vec2 = { -1, -15 }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
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
                    constantValue: vec3 = { 120, 20, 1 }
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
                            { 120, 20, 1 }
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
                            { 0.800000012, 0, 0 }
                            { 1, 1, 1 }
                            { 1.20000005, 1.5, 1.5 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin68/Particles/Aura_Self.DDS"
                numFrames: u16 = 6
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
                emitterName: string = "wind1"
                importance: u8 = 2
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 0.800000012, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, 70, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, 70, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.949999988
                    dynamics: pointer = VfxAnimatedFloatVariableData {
                        times: list[f32] = {
                            0.300000012
                            0.850000024
                        }
                        values: list[f32] = {
                            0.949999988
                            0
                        }
                    }
                }
                SpawnShape: pointer = VfxShapeSphere {
                    flags: u8 = 1
                    radius: f32 = 10
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 0, 0 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.149996191, 0.859998465, 0.140001521, 0.530006886 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                        }
                    }
                }
                pass: i16 = 100
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isDirectionOriented: flag = true
                isUniformScale: flag = true
                isRandomStartFrame: flag = true
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
                birthRotationalVelocity0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 100, 0 }
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
                            { 0, 100, 0 }
                        }
                    }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 1, 0 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.349999994
                            1
                        }
                        values: list[vec3] = {
                            { 2, 2, 2 }
                            { 2, 2, 2 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin68/Particles/Yasuo_Skin68_Q_Add_White.dds"
                numFrames: u16 = 16
                texDiv: vec2 = { 2, 2 }
            }
        }
        particleName: string = "Yasuo_Skin72_Idle_Arms_Glow"
        particlePath: string = "Characters/Yasuo/Skins/Skin72/Particles/Yasuo_Skin72_Idle_Arms_Glow"
        flags: u16 = 198
    }
}
