#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Yasuo_Skins_Skin77_Skins_Skin78_Skins_Skin79_Skins_Skin80_Skins_Skin81_Skins_Skin82_Skins_Skin83_Skins_Skin84_Skins_Skin85_Skins_Skin86.bin"
    "DATA/Characters/Yasuo/Yasuo.bin"
    "DATA/Characters/Yasuo/Animations/Skin0.bin"
    "DATA/Yasuo_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin33_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin4_Skins_Skin40_Skins_Skin41_Skins_Skin42_Skins_Skin43_Skins_Skin44_Skins_Skin45_Skins_Skin46_Skins_Skin47_Skins_Skin48_Skins_Skin49_Skins_Skin5_Skins_Skin50_Skins_Skin51_Skins_Skin52_Skins_Skin53_Skins_Skin56_Skins_Skin57_Skins_Skin58_Skins_Skin59_Skins_Skin6_Skins_Skin60_Skins_Skin61_Skins_Skin62_Skins_Skin63_Skins_Skin64_Skins_Skin65_Skins_Skin66_Skins_Skin67_Skins_Skin68_Skins_Skin69_Skins_Skin7_Skins_Skin70_Skins_Skin71_Skins_Skin72_Skins_Skin73_Skins_Skin74_Skins_Skin75_Skins_Skin76_Skins_Skin77_Skins_Skin78_Skins_Skin79_Skins_Skin8_Skins_Skin80_Skins_Skin81_Skins_Skin82_Skins_Skin83_Skins_Skin84_Skins_Skin85_Skins_Skin86.bin"
}
entries: map[hash,embed] = {
    0x2c62537b = SkinCharacterDataProperties {
        skinClassification: u32 = 2
        championSkinName: string = "YasuoSkin78"
        skinParent: i32 = 77
        metaDataTags: string = "gender:male,faction:ionia,race:human,element:wind,skinline:animasquad"
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Characters/Yasuo/Skins/Skin77/YasuoLoadScreen_77.SKINS_Yasuo_Skin77.tex"
        }
        loadscreenVintage: embed = CensoredImage {
            image: string = "ASSETS/Characters/Yasuo/Skins/Skin77/YasuoLoadScreen_77_LE.SKINS_Yasuo_Skin77.tex"
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
    0x40f3949e = StaticMaterialDef {
        name: string = "Characters/Yasuo/Skins/Skin78/Materials/Matcap_Body"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "MatCap_Tex"
                texturePath: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Yasuo_Skin77_TX_CM_MatCap.SKINS_Yasuo_Skin77.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Diffuse_Texture"
                texturePath: string = "ASSETS/Characters/Yasuo/Skins/Skin78/Yasuo_Skin78_TX_CM.Chroma_Yasuo_AnimaSquad_2024.dds"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "OutlineMask_Texture"
                texturePath: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Yasuo_Skin77_TX_CM_Mask.SKINS_Yasuo_Skin77.dds"
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "iridescentTex"
                texturePath: string = "ASSETS/Shared/Materials/EDG_Rainbow2.dds"
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "TintColor"
                value: vec4 = { 1, 1, 1, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "OutlineColor"
                value: vec4 = { 0.11999695, 0.510002315, 0.719996929, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "SpecularTintColor"
                value: vec4 = { 0.981338203, 0.996322572, 0.995666444, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "OutlineController"
                value: vec4 = { 0.200000003, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "SpecularPower"
                value: vec4 = { 1.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "WaveController"
                value: vec4 = { 1, 1, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "WaveStrength"
            }
            StaticMaterialShaderParamDef {
                name: string = "MainTexUV_Tile"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "FlipbookSize"
                value: vec4 = { 1, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Flipbook_NumberSpeed"
            }
            StaticMaterialShaderParamDef {
                name: string = "MatCap_Strength"
                value: vec4 = { 0.349999994, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "OutlineBlendValue"
            }
            StaticMaterialShaderParamDef {
                name: string = "EmissionValue"
            }
            StaticMaterialShaderParamDef {
                name: string = "OutlineMask_Strength"
                value: vec4 = { 0.800000012, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "IridescentControl"
                value: vec4 = { 0.899999976, 1, 1, 0 }
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "MATCAP_ON"
            }
            StaticMaterialSwitchDef {
                name: string = "OUTLINE_ON"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "DEFORM_ON"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "TWO_D_DEFORM_ON"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "ANIMATION_ON"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "OUTLINE_MASK_ON"
                on: bool = false
            }
            StaticMaterialSwitchDef {
                name: string = "MATCAP_MASK_ON"
            }
            StaticMaterialSwitchDef {
                name: string = "IRIDESCENCE_ON"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_R_MASK_ON_DEFORM"
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
                        shader: link = 0x13914220
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
        dynamicMaterial: pointer = DynamicMaterialDef {}
    }
    0xde49182a = StaticMaterialDef {
        name: string = "Characters/Yasuo/Skins/Skin78/Materials/HKG_MatCap_Translucent_Jelly_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "Diffuse_Texture"
                texturePath: string = "ASSETS/Characters/Yasuo/Skins/Skin78/Yasuo_Skin78_TX_CM.Chroma_Yasuo_AnimaSquad_2024.dds"
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "MatCap_Tex"
                texturePath: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Yasuo_Skin77_MatCap.SKINS_Yasuo_Skin77.dds"
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Trans_Color_Tex"
                texturePath: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Yasuo_Skin77_TibbersMCBS5.SKINS_Yasuo_Skin77.dds"
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Jelly_Diff_Mask"
                texturePath: string = "ASSETS/Shared/Materials/black.dds"
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "BlendMod"
                value: vec4 = { 1.30999994, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Alpha"
                value: vec4 = { 0.409999996, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Intensity"
                value: vec4 = { 8, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Translucent_Val"
                value: vec4 = { 1.41250002, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Nor_Direction"
                value: vec4 = { -0.200000003, 1, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Nor_Distortion"
                value: vec4 = { 0.135000005, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Nor_Lambert"
                value: vec4 = { 0.102499999, 0, 0, 0 }
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "BLEND_ALPHA"
            }
            StaticMaterialSwitchDef {
                name: string = "USE_ALPHA"
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
                        shader: link = 0x8f517ba6
                        blendEnable: bool = true
                        srcColorBlendFactor: u32 = 6
                        srcAlphaBlendFactor: u32 = 6
                        dstColorBlendFactor: u32 = 7
                        dstAlphaBlendFactor: u32 = 7
                        writeMask: u32 = 15
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
    0x7f12e5f7 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 12
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
                                    1
                                    1.29999995
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
                    1.39999998
                }
                emitterName: string = "splash_side"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -100, 0 }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 5, 3, 5 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -300, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -300, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitOffset: embed = ValueVector3 {
                        constantValue: vec3 = { 35, 0, 0 }
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
                                VfxProbabilityTableData {}
                            }
                            times: list[f32] = {
                                0
                            }
                            values: list[vec3] = {
                                { 35, 0, 0 }
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
                                            90
                                            90
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
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 40, 20 }
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
                            { 0, 40, 20 }
                        }
                    }
                }
                primitive: pointer = VfxPrimitiveArbitraryQuad {}
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.930006862 }
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
                            { 1, 1, 1, 0.930006862 }
                        }
                    }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 0.946196675, 0.956435502, 0.963164747, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.162238628
                            0.685524106
                            1
                        }
                        values: list[vec4] = {
                            { 0.946196675, 0.956435502, 0.963164747, 0 }
                            { 0.946196675, 0.956435502, 0.963164747, 1 }
                            { 0.946196675, 0.956435502, 0.963164747, 0.25 }
                            { 0.946196675, 0.956435502, 0.963164747, 0 }
                        }
                    }
                }
                pass: i16 = 6
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 2
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                0.5
                                1
                            }
                            values: list[f32] = {
                                0
                                0.600000024
                                1.60000002
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_Skin77_stack_3_mult.SKINS_Yasuo_Skin77.dds"
                }
                isDirectionOriented: flag = true
                isRandomStartFrame: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 90 }
                }
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 250, 65, 0 }
                }
                scale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.600000024, 1.04999995, 1 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.0814354718
                            0.217862427
                            0.411002368
                            0.675464451
                            1
                        }
                        values: list[vec3] = {
                            { 0.180000007, 0.314999998, 1 }
                            { 0.386794686, 0.465130568, 1 }
                            { 0.498458713, 0.638146579, 0.996892571 }
                            { 0.396631718, 0.768894374, 1 }
                            { 0.248786613, 0.894894361, 1 }
                            { 0.180000007, 0.944859862, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_Skin77_watersplashes.SKINS_Yasuo_Skin77.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 50
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
                    0.899999976
                }
                emitterName: string = "Geyser_front"
                importance: u8 = 2
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 10, -200, 10 }
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
                            { 10, -200, 10 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 7, 6, 7 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -20, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -20, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {
                    emitRotationAxes: list[vec3] = {
                        { 0, 1, 0 }
                    }
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -35, 0 }
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
                            { 0, -35, 0 }
                        }
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.127458617, 0.385091931, 1 }
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
                            { 0, 0.127458617, 0.385091931, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.223464459
                            0.687370598
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 0.447058827, 0.839215696, 0.917647064, 1 }
                            { 0.219607845, 0.458823532, 0.56078434, 0.219607845 }
                            { 0.0509803928, 0.0980392173, 0.0901960805, 0 }
                        }
                    }
                }
                pass: i16 = 52
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        constantValue: f32 = 2
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
                                0.284486085
                                0.527579367
                                1
                            }
                            values: list[f32] = {
                                0
                                0.167955562
                                0.699682593
                                2
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 2
                    erosionMapName: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_Skin77_stack_3_mult.SKINS_Yasuo_Skin77.dds"
                }
                isDirectionOriented: flag = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 30, 12, 0 }
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
                            { 30, 12, 0 }
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
                            { 1, 1, 1 }
                            { 2, 2, 1 }
                            { 2.44351459, 3, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_Skin77_Splash_2x2.SKINS_Yasuo_Skin77.dds"
                numFrames: u16 = 4
                texDiv: vec2 = { 2, 2 }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 55
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
                                    0.5
                                    3
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
                    1.45000005
                }
                emitterName: string = "DirtBits"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 100, -100, 0 }
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
                                    0.5
                                    4
                                }
                            }
                            VfxProbabilityTableData {
                                keyTimes: list[f32] = {
                                    0
                                    1
                                }
                                keyValues: list[f32] = {
                                    1
                                    0.300000012
                                }
                            }
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 100, -100, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 2, 4, 4 }
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
                            { 0, -200, 0 }
                        }
                    }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 0.200000003
                }
                0x3bf0b4ed: pointer = 0x12ab94a6 {
                    radius: f32 = 30
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 20, 0 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.560006082, 0.689997733, 1, 1 }
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
                            { 0.560006082, 0.689997733, 1, 1 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.654680014
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 50
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
                                    360
                                    -360
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
                isLocalOrientation: flag = false
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 14, 5, 5 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
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
                            VfxProbabilityTableData {}
                            VfxProbabilityTableData {}
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 14, 5, 5 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.699999988
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 0, 0, 0 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_Skin77_Bubble02.SKINS_Yasuo_Skin77.dds"
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
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterName: string = "Fresnel"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xd262fc99
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.972274363, 0.985931158, 0.990981936, 1 }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0.0650644675, 0.815976202, 0.96400398, 1 }
                    fresnel: f32 = 0.100000001
                    fresnelColor: vec4 = { 0.0921492353, 0.790859818, 0.966628492, 0 }
                }
                0xcb13aff1: f32 = -15
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00100005, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin78/Yasuo_Skin78_Recall_TX_CM.Chroma_Yasuo_AnimaSquad_2024.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 300
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                lifetime: option[f32] = {
                    1.5
                }
                emitterName: string = "TrailAdd2"
                birthVelocity: embed = ValueVector3 {
                    constantValue: vec3 = { 0, -10, 0 }
                }
                worldAcceleration: embed = IntegratedValueVector3 {
                    constantValue: vec3 = { 0, -350, 0 }
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                        }
                        values: list[vec3] = {
                            { 0, -350, 0 }
                        }
                    }
                }
                0x3bf0b4ed: pointer = 0x4f4e2ed7 {}
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mCutoff: f32 = 1000
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 400, 0, 0 }
                        }
                        mSmoothingMode: u8 = 2
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.197268635, 0.340199888, 0.819165349, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.5
                            1
                        }
                        values: list[vec4] = {
                            { 0.197268635, 0.340199888, 0.819165349, 0 }
                            { 0.197268635, 0.340199888, 0.819165349, 1 }
                            { 0.197268635, 0.340199888, 0.819165349, 1 }
                            { 0.197268635, 0.340199888, 0.819165349, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.999899983
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 0.0274509806, 0.447058827, 1, 0 }
                        }
                    }
                }
                pass: i16 = 55
                alphaRef: u8 = 0
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0.349999994
                                1
                            }
                        }
                    }
                    erosionSliceWidth: f32 = 3
                    erosionMapName: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_Skin77_Recall_Water03.SKINS_Yasuo_Skin77.dds"
                    erosionMapAddressMode: u8 = 0
                }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 95, 50, 50 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 0.5, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_Skin77_Recall_Water03.SKINS_Yasuo_Skin77.dds"
                emitterUvScrollRate: vec2 = { 0.100000001, 0 }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.100000001
                rate: embed = ValueFloat {
                    constantValue: f32 = 5
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.100000001
                        }
                    }
                }
                lifetime: option[f32] = {
                    0.349999994
                }
                emitterName: string = "Fresnel1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xd262fc99
                            0xb309c2d7
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.874326706, 1, 1 }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0.0650644675, 0.815976202, 0.96400398, 1 }
                    fresnel: f32 = 0.100000001
                    fresnelColor: vec4 = { 0.0921492353, 0.790859818, 0.966628492, 0 }
                }
                0xcb13aff1: f32 = -15
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin78/Yasuo_Skin78_Recall_TX_CM.Chroma_Yasuo_AnimaSquad_2024.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_Skin77_Q_Mis_ScanLines.SKINS_Yasuo_Skin77.dds"
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 0, -1 }
                    }
                }
            }
            VfxEmitterDefinitionData {
                timeBeforeFirstEmission: f32 = 0.800000012
                rate: embed = ValueFloat {
                    constantValue: f32 = 8
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.100000001
                    dynamics: pointer = VfxAnimatedFloatVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[f32] = {
                            0.100000001
                        }
                    }
                }
                lifetime: option[f32] = {
                    1
                }
                emitterName: string = "Fresnel2"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0xd262fc99
                            0xb309c2d7
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.874326706, 1, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.200000003
                            0.400000006
                            0.600000024
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 1 }
                            { 1, 1, 1, 0.149996191 }
                            { 0.603997886, 0, 1, 1 }
                            { 1, 1, 1, 0.209994659 }
                            { 0.571160436, 0, 1, 1 }
                            { 1, 1, 1, 0.149996191 }
                        }
                    }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0.0650644675, 0.815976202, 0.96400398, 1 }
                    fresnel: f32 = 0.100000001
                    fresnelColor: vec4 = { 0.0921492353, 0.790859818, 0.966628492, 0 }
                }
                0xcb13aff1: f32 = -15
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin78/Yasuo_Skin78_Recall_TX_CM.Chroma_Yasuo_AnimaSquad_2024.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_Skin77_Q_Mis_ScanLines.SKINS_Yasuo_Skin77.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 1, 0.800000012 }
                    }
                }
            }
        }
        particleName: string = "Yasuo_Skin78_Recall_Fish02"
        particlePath: string = "Characters/Yasuo/Skins/Skin78/Particles/Yasuo_Skin78_Recall_Fish02"
        flags: u16 = 197
    }
    0xb3304a14 = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterName: string = "Fresnel1"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0x09632d04
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0.259998471, 1, 1 }
                }
                pass: i16 = 1
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0.589593351, 0.0650644675, 0.96400398, 1 }
                    fresnel: f32 = 0.0299999993
                    fresnelColor: vec4 = { 0.553582072, 0.0921492353, 0.966628492, 0 }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00100005, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_Skin77_TX_CM_Sword01.SKINS_Yasuo_Skin77.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterName: string = "Fresnel2"
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
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0, 0, 0, 1 }
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 1, 0.439017326, 0.683787286, 1 }
                    fresnel: f32 = 0.0500000007
                    fresnelColor: vec4 = { 0.966628492, 0.0921492353, 0.465110242, 0 }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00999999, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_R_Buff_Hair002.SKINS_Yasuo_Skin77.dds"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterName: string = "Fresnel3"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { 6, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0x09632d04
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.258381009, 0.791683853, 0.98892194, 1 }
                }
                pass: i16 = 1000
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0.589593351, 0.0650644675, 0.96400398, 1 }
                    fresnel: f32 = 0.0299999993
                    fresnelColor: vec4 = { 0.553582072, 0.0921492353, 0.966628492, 0 }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_Skin77_TX_CM_Sword01.SKINS_Yasuo_Skin77.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_Skin77_Dot02.SKINS_Yasuo_Skin77.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 150, 150 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 5, 1 }
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
                particleLinger: option[f32] = {}
                lifetime: option[f32] = {
                    0.300000012
                }
                isSingleParticle: flag = true
                emitterName: string = "Fresnel4"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                0x563d4a22: embed = ValueVector3 {
                    constantValue: vec3 = { -6, 0, 0 }
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            0x09632d04
                        }
                        mLockMeshToAttachment: bool = true
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.258381009, 0.791683853, 0.98892194, 1 }
                }
                pass: i16 = 1000
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0.589593351, 0.0650644675, 0.96400398, 1 }
                    fresnel: f32 = 0.0299999993
                    fresnelColor: vec4 = { 0.553582072, 0.0921492353, 0.966628492, 0 }
                }
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                hasPostRotateOrientation: flag = true
                isRotationEnabled: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.00300002, 1, 1 }
                }
                texture: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_Skin77_TX_CM_Sword01.SKINS_Yasuo_Skin77.dds"
                textureMult: pointer = 0xb097c1bd {
                    textureMult: string = "ASSETS/Characters/Yasuo/Skins/Skin77/Particles/Yasuo_Skin77_Dot02.SKINS_Yasuo_Skin77.dds"
                    uvScaleMult: embed = ValueVector2 {
                        constantValue: vec2 = { 150, 150 }
                    }
                    birthUvScrollRateMult: embed = ValueVector2 {
                        constantValue: vec2 = { 5, 1 }
                    }
                }
            }
        }
        particleName: string = "Yasuo_Skin78_I_Sword"
        particlePath: string = "Characters/Yasuo/Skins/Skin78/Particles/Yasuo_Skin78_I_Sword"
        flags: u16 = 197
    }
    0xf14d4ce9 = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Yasuo_BA_Crit_hit_01" = 0xd567e3bf
            "Yasuo_BA_Crit_hit_02" = 0xd667e552
            "Yasuo_BA_Crit_hit_03" = 0xd767e6e5
            "Yasuo_BA_Crit_hit_04" = 0xd067dbe0
            "Yasuo_BA_hit_tar_01" = 0xe48cfa0c
            "Yasuo_BA_hit_tar_02" = 0xe78cfec5
            "Yasuo_BA_hit_tar_03" = 0xe68cfd32
            "Yasuo_BA_hit_tar_04" = 0xe18cf553
            "Yasuo_BA_trail_1" = 0xaa35fa2b
            "Yasuo_BA_trail_2" = 0xab35fbbe
            "Yasuo_BA_trail_3" = 0xac35fd51
            "Yasuo_BA_trail_4" = 0xad35fee4
            "Yasuo_Dance_flute_wind" = 0x72a890ec
            0x635797df = 0xc2808613
            "Yasuo_Emote_dance_in_sound" = 0x0ef7df83
            "Yasuo_Emote_dance_sound" = 0xc6a1736b
            "Yasuo_Emote_death_sound" = 0x13f96112
            "Yasuo_Emote_joke_sound" = 0x0bd319ab
            "Yasuo_Emote_laugh_sound" = 0xb5dd93bd
            "Yasuo_Emote_taunt2_sound" = 0x158a6b62
            "Yasuo_Emote_taunt_generic" = 0x377112ca
            "Yasuo_Emote_taunt_interactive_ninja" = 0xba636348
            "Yasuo_Emote_taunt_interactive_riven" = 0xec34fa42
            "Yasuo_Emote_taunt_interactive_yi" = 0x6e248f72
            "Yasuo_Emote_taunt_sound" = 0x86bc33c4
            "Yasuo_EQ3_cas" = 0x819362ee
            "Yasuo_EQ_cas" = 0x0fd1a365
            "Yasuo_EQ_SwordGlow" = 0x8fdf464c
            "Yasuo_E_Dash" = 0x68c0b7a5
            "Yasuo_E_dash_hit" = 0x8b5ce64f
            "Yasuo_E_timer1" = 0xea5d6759
            "Yasuo_E_timer2" = 0xe75d62a0
            "Yasuo_E_timer3" = 0xe85d6433
            "Yasuo_E_timer4" = 0xed5d6c12
            "Yasuo_E_timer5" = 0xee5d6da5
            "Yasuo_I_sheath_spark" = 0xcc81c732
            "Yasuo_NightmareBot_E_timer1" = 0xea5d6759
            "Yasuo_NightmareBot_E_timer2" = 0xe75d62a0
            "Yasuo_NightmareBot_E_timer3" = 0xe85d6433
            "Yasuo_NightmareBot_E_timer4" = 0xed5d6c12
            "Yasuo_NightmareBot_E_timer5" = 0xee5d6da5
            "Yasuo_Passive_Activate" = 0x2825eb16
            "Yasuo_Passive_Burst" = 0x251801ff
            "Yasuo_Q3_Hand" = 0x1919ce43
            "Yasuo_Q3_Indicator_Ring" = 0xc91a56a6
            "Yasuo_Q3_Indicator_Ring_alt" = 0xe67dbf16
            "Yasuo_Q_Hand" = 0x5468595c
            "Yasuo_Q_hit_tar" = 0xff235b22
            "Yasuo_Q_sound" = 0x989cdc78
            "Yasuo_Q_WindStrike" = 0xf8656941
            "Yasuo_Q_WindStrike_02" = 0x10b28364
            "Yasuo_Q_wind_hit_tar" = 0xc76a2099
            "Yasuo_Q_wind_mis" = 0xe529d917
            "Yasuo_Q_wind_ready_buff" = 0xd2ef7805
            0xc542e434 = 0xa74ae7e8
            0x36a5a16b = 0x66a05e7f
            "Yasuo_R_cantcast_beam" = 0xde4cabd7
            "Yasuo_R_cas_marker_01" = 0xce1126e0
            "Yasuo_R_CloneVFX" = 0x20a71fc9
            "Yasuo_R_dash" = 0x94ea1dfe
            "Yasuo_R_impact_tar" = 0x3dac7fc0
            "Yasuo_R_indicator_beam" = 0x0ed54a43
            "Yasuo_R_land_tar" = 0x59bdb1e7
            "Yasuo_R_slash_cas" = 0xbabb7bb5
            "Yasuo_R_SwordGlow" = 0x2ca9c0be
            "Yasuo_R_tar_imp_01" = 0x4fd6da7a
            0xf90ee152 = 0xfa887166
            0xf80edfbf = 0xf9886fd3
            "Yasuo_Taunt_spit" = 0x79dc2bba
            "Yasuo_Wall_XinZhao_OLD" = 0xcbdbe965
            "Yasuo_W_windwall1" = 0x7ffe74ec
            "Yasuo_W_windwall2" = 0x82fe79a5
            "Yasuo_W_windwall3" = 0x81fe7812
            "Yasuo_W_windwall4" = 0x7cfe7033
            "Yasuo_W_windwall5" = 0x7bfe6ea0
            "Yasuo_W_windwall_activate" = 0x195e85af
            "Yasuo_W_Windwall_big_impact" = 0xc1465e5f
            "Yasuo_W_windwall_enemy_01" = 0xf1cf00bc
            "Yasuo_W_windwall_enemy_02" = 0xf4cf0575
            "Yasuo_W_windwall_enemy_03" = 0xf3cf03e2
            "Yasuo_W_windwall_enemy_04" = 0xeecefc03
            "Yasuo_W_windwall_enemy_05" = 0xedcefa70
            "Yasuo_Q_Odyssey_Wandering_wind_mis" = 0xe529d917
            "Yasuo_Q_Odyssey_Growing_wind_mis" = 0xe529d917
            "Yasuo_Q_Odyssey_Wandering_Growing_wind_mis" = 0xe529d917
            0xc3bc76ee = 0xacac2bba
            0xc2bc755b = 0xabac2a27
            0xc1bc73c8 = 0xaaac2894
            0xc8bc7ecd = 0xa9ac2701
            0x3518fb5d = 0x00000000
            0x7d830716 = 0x8ab2981a
            0x5362ed1a = 0x8d6dfffe
            0x5262eb87 = 0x8c6dfe6b
            0x5162e9f4 = 0x8b6dfcd8
            0x5062e861 = 0x926e07dd
            0xaf6c1a5c = 0xc0be9518
            0x11a31bc1 = 0x8b1f731d
            0x0ebb58bb = 0x918c307f
            0x9abf5dc0 = 0x04f0f554
            0xf42dabe5 = 0x23d5dff1
            0xf32daa52 = 0x22d5de5e
            0x6aeac89c = 0x057d82b8
            0x6deacd55 = 0x7f12e5f7
            0x12155abd = 0x79826b39
            0x9670a962 = 0xf6f1e1a6
            0x11c02186 = 0xb3304a14
            0x3712807c = 0x502a7c98
            0xe9795bed = 0x192e7290
        }
    }
}
