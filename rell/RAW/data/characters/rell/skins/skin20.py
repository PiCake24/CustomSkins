#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Rell_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29.bin"
    "DATA/Characters/Rell/Rell.bin"
    "DATA/Characters/Rell/Animations/Skin20.bin"
    "DATA/Rell_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin10_Skins_Skin11_Skins_Skin12_Skins_Skin13_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin2_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin4_Skins_Skin5_Skins_Skin6_Skins_Skin7_Skins_Skin8_Skins_Skin9.bin"
}
entries: map[hash,embed] = {
    "Characters/Rell/Skins/Skin20" = SkinCharacterDataProperties {
        skinClassification: u32 = 1
        championSkinName: string = "RellSkin20"
        metaDataTags: string = "faction:noxus,gender:female,race:human,skinline:highnoon"
        skinUpgradeData: embed = skinUpgradeData {
            mGearSkinUpgrades: list[link] = {
                0xdc516595
                0xa1b84763
            }
        }
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Characters/Rell/Skins/Skin20/RellLoadScreen_20.tex"
        }
        loadscreenVintage: embed = CensoredImage {
            image: string = "ASSETS/Characters/Rell/Skins/Skin20/RellLoadScreen_20_LE.tex"
        }
        skinAudioProperties: embed = skinAudioProperties {
            tagEventList: list[string] = {
                "Rell"
                "RellSkin20"
            }
            bankUnits: list2[embed] = {
                BankUnit {
                    name: string = "Rell_Base_VO"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Rell/Skins/Base/Rell_Base_VO_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Rell/Skins/Base/Rell_Base_VO_events.bnk"
                        "ASSETS/Sounds/Wwise2016/VO/en_US/Characters/Rell/Skins/Base/Rell_Base_VO_audio.wpk"
                    }
                    events: list[string] = {
                        "Play_vo_Rell_Assist3DGeneral"
                        "Play_vo_Rell_Attack2DGeneral"
                        "Play_vo_Rell_Death3D"
                        "Play_vo_Rell_FirstEncounter3DCassiopeia"
                        "Play_vo_Rell_FirstEncounter3DDarius"
                        "Play_vo_Rell_FirstEncounter3DEkko"
                        "Play_vo_Rell_FirstEncounter3DElise"
                        "Play_vo_Rell_FirstEncounter3DKled"
                        "Play_vo_Rell_FirstEncounter3DLeblanc"
                        "Play_vo_Rell_FirstEncounter3DLeona"
                        "Play_vo_Rell_FirstEncounter3DMordekaiser"
                        "Play_vo_Rell_FirstEncounter3DSamira"
                        "Play_vo_Rell_FirstEncounter3DSeraphine"
                        "Play_vo_Rell_FirstEncounter3DSett"
                        "Play_vo_Rell_FirstEncounter3DSwain"
                        "Play_vo_Rell_Joke3DGeneral"
                        "Play_vo_Rell_JokeResponse3DGeneral"
                        "Play_vo_Rell_Kill3DCassiopeia"
                        "Play_vo_Rell_Kill3DDarius"
                        "Play_vo_Rell_Kill3DEkko"
                        "Play_vo_Rell_Kill3DElise"
                        "Play_vo_Rell_Kill3DGeneral"
                        "Play_vo_Rell_Kill3DKled"
                        "Play_vo_Rell_Kill3DLeblanc"
                        "Play_vo_Rell_Kill3DLeona"
                        "Play_vo_Rell_Kill3DMordekaiser"
                        "Play_vo_Rell_Kill3DPentakill"
                        "Play_vo_Rell_Kill3DSamira"
                        "Play_vo_Rell_Kill3DSeraphine"
                        "Play_vo_Rell_Kill3DSett"
                        "Play_vo_Rell_Kill3DSwain"
                        "Play_vo_Rell_Laugh3DGeneral"
                        "Play_vo_Rell_Move2DFirst"
                        "Play_vo_Rell_Move2DLong"
                        "Play_vo_Rell_Move2DStandard"
                        "Play_vo_Rell_Recall3DGeneral"
                        "Play_vo_Rell_RellBasicAttack2_cast3D"
                        "Play_vo_Rell_RellBasicAttack_cast3D"
                        "Play_vo_Rell_RellE_cast3D"
                        "Play_vo_Rell_RellQ_cast3D"
                        "Play_vo_Rell_RellR_cast3D"
                        "Play_vo_Rell_RellW_Dismount_cast3D"
                        "Play_vo_Rell_RellW_MountUp_cast3D"
                        "Play_vo_Rell_Respawn2DGeneral"
                        "Play_vo_Rell_Taunt3DGeneral"
                        "Play_vo_Rell_TauntResponse3DGeneral"
                    }
                    voiceOver: bool = true
                }
                BankUnit {
                    name: string = "Rell_Skin20_SFX"
                    bankPath: list[string] = {
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Rell/Skins/Skin20/Rell_Skin20_SFX_audio.bnk"
                        "ASSETS/Sounds/Wwise2016/SFX/Characters/Rell/Skins/Skin20/Rell_Skin20_SFX_events.bnk"
                    }
                    events: list[string] = {
                        "Play_sfx_RellSkin20_Dance3D_cast"
                        "Play_sfx_RellSkin20_Dance3D_jump"
                        "Play_sfx_RellSkin20_Dance3D_lance"
                        "Play_sfx_RellSkin20_Dance3D_loop"
                        "Play_sfx_RellSkin20_Death3D_Biped_cast"
                        "Play_sfx_RellSkin20_Death3D_Mounted_cast"
                        "Play_sfx_RellSkin20_Joke3D_cast"
                        "Play_sfx_RellSkin20_Joke3D_loop"
                        "Play_sfx_RellSkin20_Laugh3D_Biped_cast"
                        "Play_sfx_RellSkin20_Laugh3D_Mounted_cast"
                        "Play_sfx_RellSkin20_Recall3D_Biped_cast"
                        "Play_sfx_RellSkin20_Recall3D_Mounted_cast"
                        "Play_sfx_RellSkin20_RellBasicAttack2_OnCast"
                        "Play_sfx_RellSkin20_RellBasicAttack2_OnHit"
                        "Play_sfx_RellSkin20_RellBasicAttack_OnCast"
                        "Play_sfx_RellSkin20_RellBasicAttack_OnHit"
                        "Play_sfx_RellSkin20_RellCritAttack_OnCast"
                        "Play_sfx_RellSkin20_RellCritAttack_OnHit"
                        "Play_sfx_RellSkin20_RellE_buffactivate"
                        "Play_sfx_RellSkin20_RellE_empowered_hit"
                        "Play_sfx_RellSkin20_RellE_footstep_buffactivate"
                        "Play_sfx_RellSkin20_RellE_footstep_mute"
                        "Play_sfx_RellSkin20_RellE_OnCast"
                        "Play_sfx_RellSkin20_RellE_RampSpeed_buffactivate"
                        "Play_sfx_RellSkin20_RellP_debuff_maxstack_buffactivate"
                        "Play_sfx_RellSkin20_RellQ_hit"
                        "Play_sfx_RellSkin20_RellQ_idleout"
                        "Play_sfx_RellSkin20_RellQ_OnCast"
                        "Play_sfx_RellSkin20_RellQ_ShieldBreak_hit"
                        "Play_sfx_RellSkin20_RellR_Damage_OnBuffCast"
                        "Play_sfx_RellSkin20_RellR_DamageZone_OnBuffCast"
                        "Play_sfx_RellSkin20_RellR_OnCast"
                        "Play_sfx_RellSkin20_RellW_Dismount_hit"
                        "Play_sfx_RellSkin20_RellW_Dismount_land"
                        "Play_sfx_RellSkin20_RellW_Dismount_OnBuffActivate"
                        "Play_sfx_RellSkin20_RellW_Dismount_OnCast"
                        "Play_sfx_RellSkin20_RellW_EmpoweredAttack_cast"
                        "Play_sfx_RellSkin20_RellW_EmpoweredAttack_hit"
                        "Play_sfx_RellSkin20_RellW_MountUp_OnBuffActivate"
                        "Play_sfx_RellSkin20_RellW_MountUp_OnBuffCast"
                        "Play_sfx_RellSkin20_RellW_MountUp_OnBuffDeactivate"
                        "Play_sfx_RellSkin20_RellW_MountUp_OnCast"
                        "Play_sfx_RellSkin20_Respawn3D_buffactivate"
                        "Play_sfx_RellSkin20_Taunt3D_cast"
                        "Play_sfx_RellSkin20_Winddown3D_buffactivate"
                        "Stop_sfx_RellSkin20_RellE_buffactivate"
                        "Stop_sfx_RellSkin20_RellE_footstep_buffactivate"
                        "Stop_sfx_RellSkin20_RellE_loop_buffactivate"
                        "Stop_sfx_RellSkin20_RellE_RampSpeed_buffactivate"
                    }
                }
            }
        }
        skinAnimationProperties: embed = skinAnimationProperties {
            animationGraphData: link = 0xb6617d0b
        }
        skinMeshProperties: embed = SkinMeshDataProperties {
            skeleton: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20.skl"
            simpleSkin: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20.skn"
            texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_TX_CM.tex"
	 	 	skinScale: f32 = 2
            selfIllumination: f32 = 0.699999988
            overrideBoundingBox: option[vec3] = {
                { 283.25, 230.619995, 283.25 }
            }
            initialSubmeshToHide: string = "LanceMetal Armor_Shoulder Armor_Leg Armor_Leg_Mid Armor_Leg_Lower Armor_Gauntlet Armor_Foot Armor_Chest JokeHorsie JokeHorsie_Stand Hands_MAT"
            materialOverride: list[embed] = {
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_Lance_TX_CM.tex"
                    submesh: string = "Lance"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_Horse_TX_CM.tex"
                    submesh: string = "Horse_Tail"
                }
                SkinMeshDataProperties_MaterialOverride {
                    material: link = "Characters/Rell/Skins/Skin20/Materials/Rell_LanceMental"
                    submesh: string = "LanceMetal"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_Horse_TX_CM.tex"
                    submesh: string = "Horse_BackLegs"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_Horse_TX_CM.tex"
                    submesh: string = "Horse_Head"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_Horse_TX_CM.tex"
                    submesh: string = "Horse_Midsection"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_Horse_TX_CM.tex"
                    submesh: string = "Horse_FrontLegs"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_Horse_TX_CM.tex"
                    submesh: string = "Horse_Rear"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_Horse_TX_CM.tex"
                    submesh: string = "Horse_Saddle"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_Horse_TX_CM.tex"
                    submesh: string = "JokeHorsie"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_HorsieStand_TX_CM.tex"
                    submesh: string = "JokeHorsie_Stand"
                }
                SkinMeshDataProperties_MaterialOverride {
                    material: link = "Characters/Rell/Skins/Skin20/Materials/Rell_Horse_VFX"
                    submesh: string = "Horse_Vfxbody"
                }
                SkinMeshDataProperties_MaterialOverride {
                    material: link = "Characters/Rell/Skins/Skin20/Materials/Rell_Horse_VFX"
                    submesh: string = "Horse_Vfxtail"
                }
                SkinMeshDataProperties_MaterialOverride {
                    material: link = "Characters/Rell/Skins/Skin20/Materials/Specular_Fresnel_Masked_inst"
                    submesh: string = "Body"
                }
                SkinMeshDataProperties_MaterialOverride {
                    texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_Horse_TX_CM.tex"
                    submesh: string = "Horse_Horns"
                }
                SkinMeshDataProperties_MaterialOverride {
                    material: link = "Characters/Rell/Skins/Skin20/Materials/Rell_Hands"
                    submesh: string = "Hands_MAT"
                }
                SkinMeshDataProperties_MaterialOverride {
                    material: link = "Characters/Rell/Skins/Skin20/Materials/Rell_VFXNeck_inst"
                    submesh: string = "Horse_Vfxneck"
                }
            }
            rigPoseModifierData: list[pointer] = {
                ConformToPathRigPoseModifierData {
                    mStartingJointName: hash = "H_Spine3_Ground"
                    mEndingJointName: hash = "H_Pelvis_Ground"
                    mDefaultMaskName: hash = 0x97dc0b10
                    mMaxBoneAngle: f32 = 35
                    mDampingValue: f32 = 15
                }
                ConformToPathRigPoseModifierData {
                    mStartingJointName: hash = "H_Tail1"
                    mEndingJointName: hash = "H_Tail6"
                    mDefaultMaskName: hash = 0x97dc0b10
                    mMaxBoneAngle: f32 = 35
                }
            }
        }
        armorMaterial: string = "Metal"
        defaultAnimations: list[string] = {
            "Idle1Props"
        }
        mContextualActionData: link = "Characters/Rell/CAC/Rell_Base"
        iconCircle: option[string] = {
            "ASSETS/Characters/Rell/HUD/Rell_Circle_0.tex"
        }
        iconSquare: option[string] = {
            "ASSETS/Characters/Rell/HUD/Rell_Square.tex"
        }
        iconAvatar: string = "ASSETS/Characters/Rell/HUD/Rell_Circle_20.tex"
        healthBarData: embed = CharacterHealthBarDataRecord {
            attachToBone: string = "BuffBone_Cstm_Healthbar"
            unitHealthBarStyle: u8 = 12
        }
        mResourceResolver: link = "Characters/Rell/Skins/Skin20/Resources"
        PersistentEffectConditions: list2[pointer] = {
            PersistentEffectConditionData {
                OwnerCondition: pointer = HasBuffDynamicMaterialBoolDriver {
                    Spell: hash = 0x38ee07f5
                }
                PersistentVfxs: list2[embed] = {
                    PersistentVfxData {
                        effectKey: hash = 0x799c2c66
                    }
                }
            }
            PersistentEffectConditionData {
                OwnerCondition: pointer = NotMaterialDriver {
                    mDriver: pointer = OneTrueMaterialDriver {
                        mDrivers: list[pointer] = {
                            HasGearDynamicMaterialBoolDriver {
                                mGearIndex: u8 = 1
                            }
                            IsAnimationPlayingDynamicMaterialBoolDriver {
                                mAnimationNames: list[hash] = {
                                    "Joke_Intro"
                                    "death"
                                    "Joke_Cycle"
                                }
                            }
                            HasBuffDynamicMaterialBoolDriver {
                                Spell: hash = "Shared/Spells/ZhonyasRingShield"
                            }
                            NotMaterialDriver {
                                mDriver: pointer = SubmeshVisibilityBoolDriver {
                                    AnySubmesh: bool = false
                                    Submeshes: list[hash] = {
                                        "Horse_Vfxneck"
                                    }
                                }
                            }
                        }
                    }
                }
                PersistentVfxs: list2[embed] = {
                    PersistentVfxData {
                        boneName: string = "H_Neck_Helper"
                        effectKey: hash = "Rell_Idle_Body_Glow1"
                    }
                }
            }
            PersistentEffectConditionData {
                OwnerCondition: pointer = HasBuffDynamicMaterialBoolDriver {
                    Spell: hash = 0x38ee07f5
                }
                PersistentVfxs: list2[embed] = {
                    PersistentVfxData {
                        boneName: string = "C_Buffbone_Glb_Chest_Loc"
                        effectKey: hash = "Rell_E_buff"
                    }
                }
            }
            PersistentEffectConditionData {
                OwnerCondition: pointer = HasBuffDynamicMaterialBoolDriver {
                    Spell: hash = 0x38ee07f5
                }
                PersistentVfxs: list2[embed] = {
                    PersistentVfxData {
                        boneName: string = "Lance_Part4"
                        effectKey: hash = "Rell_E_Stage3"
                    }
                }
            }
            PersistentEffectConditionData {
                OwnerCondition: pointer = HasBuffDynamicMaterialBoolDriver {
                    Spell: hash = 0x7ea6dadf
                }
                PersistentVfxs: list2[embed] = {
                    PersistentVfxData {
                        boneName: string = "Lance_Base"
                        effectKey: hash = "Rell_E_Empowered_Lance"
                    }
                }
            }
        }
    }
    "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Mount_Transform_Child" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.400000006
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Darkunderglow_kayn"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 20, 0, 80 }
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
                    constantValue: vec4 = { 0.0392156877, 0.0431372561, 0.0666666701, 1 }
                }
                color: embed = ValueColor {
                    constantValue: vec4 = { 1, 1, 1, 0.659998477 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.899999976
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0.659998477 }
                            { 1, 1, 1, 0.659998477 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 0, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 150, 50, 0 }
                }
                texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Glow.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 300
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.300000012
                }
                particleLinger: option[f32] = {
                    0.300000012
                }
                lifetime: option[f32] = {
                    0.850000024
                }
                rateByVelocityFunction: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 0 }
                }
                emitterName: string = "Ribbon_"
                importance: u8 = 0
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 30, 10 }
                }
                primitive: pointer = VfxPrimitiveCameraTrail {
                    mTrail: embed = VfxTrailDefinitionData {
                        mMode: u8 = 1
                        mBirthTilingSize: embed = ValueVector3 {
                            constantValue: vec3 = { 500, 0, 0 }
                        }
                        mSmoothingMode: u8 = 1
                        mMaxAddedPerFrame: i32 = 15
                    }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.282352954, 0, 1 }
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.800000012
                            1
                        }
                        values: list[vec4] = {
                            { 1, 0.282352954, 0, 0 }
                            { 1, 0.282352954, 0, 1 }
                            { 1, 0.282352954, 0, 1 }
                            { 1, 0.282352954, 0, 0 }
                        }
                    }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            0.75
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 0.968627453, 0.792156875, 1 }
                            { 1, 0.970000744, 0.790005326, 0.349996179 }
                            { 0.898039222, 0.450980395, 0.0823529437, 0 }
                        }
                    }
                }
                pass: i16 = -10
                miscRenderFlags: u8 = 1
                isUniformScale: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 90, 1, 1 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.100000001
                            1
                        }
                        values: list[vec3] = {
                            { 1, 1, 1 }
                            { 1, 1, 1 }
                            { 1.20000005, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Whisp_Gray_Horizontal.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Chromatic_Abberation_Noise.tex"
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
                    0.349999994
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Metal_Head1"
                birthVelocity: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {
                    emitOffset: vec3 = { 0, 20, 80 }
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
                        mSimpleMeshName: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Horse_Head.scb"
                    }
                }
                blendMode: u8 = 3
                pass: i16 = 6
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                -1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Horse_Erode_Swipe.tex"
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0.827450991, 0.796078444, 0.709803939, 1 }
                    fresnel: f32 = 0.00999999978
                    fresnelColor: vec4 = { 0.960784316, 0.227450982, 0.0235294122, 0 }
                }
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
                isRotationEnabled: flag = true
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 0.5, 1, 0.699999988 }
                }
                texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_Horse_TX_CM.tex"
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 0.5
                }
                particleLinger: option[f32] = {
                    0.349999994
                }
                lifetime: option[f32] = {
                    1
                }
                isSingleParticle: flag = true
                emitterName: string = "Metal_Shoulder1"
                birthVelocity: embed = ValueVector3 {
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
                            { 0, 0, 0 }
                        }
                    }
                }
                birthDrag: embed = ValueVector3 {
                    constantValue: vec3 = { 3, 3, 3 }
                }
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
                primitive: pointer = VfxPrimitiveMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSimpleMeshName: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Horse_Shoulders_ma.scb"
                    }
                }
                blendMode: u8 = 3
                pass: i16 = 5
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0.800000012
                                1
                            }
                            values: list[f32] = {
                                0
                                1
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Chromatic_Abberation_Noise.tex"
                }
                reflectionDefinition: pointer = VfxReflectionDefinitionData {
                    reflectionFresnelColor: vec4 = { 0.827450991, 0.796078444, 0.709803939, 1 }
                    fresnel: f32 = 0.00999999978
                    fresnelColor: vec4 = { 0.243137255, 0.23137255, 0.152941182, 0 }
                }
                miscRenderFlags: u8 = 1
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
                birthRotation0: embed = ValueVector3 {
                    constantValue: vec3 = { 0, 180, 0 }
                }
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 1.25, 1.25, 1.25 }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                        }
                        values: list[vec3] = {
                            { 1, 1, 0 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_Horse_TX_CM.tex"
            }
        }
        particleName: string = "Rell_Skin20_W_Mount_Transform_Child"
        particlePath: string = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Mount_Transform_Child"
    }
    "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Idle_Body_Glow1" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = -1
                }
                particleLinger: option[f32] = {
                    0.400000006
                }
                isSingleParticle: flag = true
                childParticleSetDefinition: pointer = VfxChildParticleSetDefinitionData {
                    childrenIdentifiers: list[embed] = {
                        VfxChildIdentifier {
                            effectKey: hash = "Rell_Idle_Body_Glow"
                        }
                    }
                }
                emitterName: string = "Temp_Avatar"
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { -25, -20, 0 }
                }
                primitive: pointer = VfxPrimitiveAttachedMesh {}
                meshRenderFlags: u8 = 0
                alphaRef: u8 = 0
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                isUniformScale: flag = true
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
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
                            2
                        }
                    }
                }
                emitterName: string = "BaseEnergyBlend"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {}
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "Horse_Vfxneck"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                    AlignPitchToCamera: bool = true
                    AlignYawToCamera: bool = true
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/common_color-hold.Leblanc_Rework.dds"
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.529411793, 0.113725491, 0.0392156877, 1 }
                }
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
                            { 1, 1, 1, 0.501960814 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 99
                0xcb13aff1: f32 = -0.100000001
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_Beam_03.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.200000003 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
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
                            { 1, 1 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.800000012, 1 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Idle_Mask.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 3
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
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
                            2
                        }
                    }
                }
                emitterName: string = "BaseEnergyBlend1"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {}
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "Horse_Vfxneck"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                    AlignPitchToCamera: bool = true
                    AlignYawToCamera: bool = true
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/common_color-hold.Leblanc_Rework.dds"
                blendMode: u8 = 1
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 0.137254909, 0.152941182, 0.239215687, 1 }
                }
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
                            { 1, 1, 1, 0.501960814 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 70
                0xcb13aff1: f32 = -0.100000001
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_Beam_03.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.200000003 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
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
                            { 1, 1 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 0.5, 1 }
                }
                uvTransformCenter: vec2 = { 0.400000006, 0.5 }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Idle_Mask.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
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
                            2
                        }
                    }
                }
                emitterName: string = "BaseEnergyBlend2"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {}
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "Horse_Vfxneck"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                    AlignPitchToCamera: bool = true
                    AlignYawToCamera: bool = true
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/common_color-hold.Leblanc_Rework.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.7400015, 0.0800030529, 0.340001523 }
                }
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
                            { 1, 1, 1, 0.501960814 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 100
                0xcb13aff1: f32 = -0.100000001
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_Beam_03.tex"
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0, 0.200000003 }
                    dynamics: pointer = VfxAnimatedVector2fVariableData {
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
                        }
                        times: list[f32] = {
                            0
                        }
                        values: list[vec2] = {
                            { 0, 0.200000003 }
                        }
                    }
                }
                birthUVOffset: embed = ValueVector2 {
                    constantValue: vec2 = { 1, 1 }
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
                            { 1, 1 }
                        }
                    }
                }
                uvScale: embed = ValueVector2 {
                    constantValue: vec2 = { 1.5, 1 }
                }
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Idle_Mask.tex"
                }
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 2
                }
                particleLifetime: embed = ValueFloat {
                    constantValue: f32 = 2
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
                            2
                        }
                    }
                }
                emitterName: string = "BaseEnergyBlend3"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = 0xee39916f {}
                primitive: pointer = VfxPrimitiveAttachedMesh {
                    mMesh: embed = VfxMeshDefinitionData {
                        mSubmeshesToDraw: list[hash] = {
                            "Horse_Vfxneck"
                        }
                        mLockMeshToAttachment: bool = true
                    }
                    AlignPitchToCamera: bool = true
                    AlignYawToCamera: bool = true
                }
                particleColorTexture: string = "ASSETS/Shared/Particles/common_color-hold.Leblanc_Rework.dds"
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.179995418, 0.0200045779, 0.2399939 }
                }
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
                            { 1, 1, 1, 0.501960814 }
                            { 1, 1, 1, 0 }
                        }
                    }
                }
                pass: i16 = 150
                disableBackfaceCull: bool = true
                particleIsLocalOrientation: flag = true
                texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/common_Aura_Self.tex"
                textureMult: pointer = VfxTextureMultDefinitionData {
                    textureMult: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Idle_Mask.tex"
                }
            }
        }
        visibilityRadius: f32 = 99999
        particleName: string = "Rell_Skin20_Idle_Body_Glow1"
        particlePath: string = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Idle_Body_Glow1"
    }
    "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Idle_Body_Glow" = VfxSystemDefinitionData {
        complexEmitterDefinitionData: list[pointer] = {
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
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
                                    0.600000024
                                    2
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
                emitterName: string = "Flames_Head1"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 70, 15, 10 }
                }
                EmitterPosition: embed = ValueVector3 {
                    constantValue: vec3 = { 20, 0, 0 }
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
                            0.600000024
                            1
                        }
                        values: list[vec4] = {
                            { 1, 1, 1, 0 }
                            { 1, 1, 1, 1 }
                            { 1, 0.392156869, 0.349019617, 1 }
                            { 1, 0.274509817, 0.274509817, 0 }
                        }
                    }
                }
                pass: i16 = 110
                alphaErosionDefinition: pointer = VfxAlphaErosionDefinitionData {
                    erosionDriveCurve: embed = ValueFloat {
                        dynamics: pointer = VfxAnimatedFloatVariableData {
                            times: list[f32] = {
                                0
                                1
                            }
                            values: list[f32] = {
                                0
                                2
                            }
                        }
                    }
                    erosionMapName: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Noise4.tex"
                }
                0xcb13aff1: f32 = -0.100000001
                particleIsLocalOrientation: flag = true
                isRotationEnabled: flag = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 8, 8, 8 }
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
                            { 8, 8, 8 }
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
                            { 0.5, 0.5, 0.5 }
                            { 2, 2, 2 }
                            { 2, 2, 2 }
                            { 3, 3, 3 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Flame.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 0.550000012 }
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
                            { 0.25, 0.550000012 }
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
            }
            VfxEmitterDefinitionData {
                rate: embed = ValueFloat {
                    constantValue: f32 = 100
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
                                    0.600000024
                                    2
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
                emitterName: string = "Flames_Head2"
                importance: u8 = 2
                bindWeight: embed = ValueFloat {
                    constantValue: f32 = 1
                }
                SpawnShape: pointer = VfxShapeBox {
                    flags: u8 = 1
                    Size: vec3 = { 80, 15, 10 }
                }
                blendMode: u8 = 4
                birthColor: embed = ValueColor {
                    constantValue: vec4 = { 1, 0.717647076, 0.00784313772, 1 }
                }
                color: embed = ValueColor {
                    dynamics: pointer = VfxAnimatedColorVariableData {
                        times: list[f32] = {
                            0
                            0.300000012
                            0.400000006
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
                pass: i16 = 120
                0xcb13aff1: f32 = -0.100000001
                particleIsLocalOrientation: flag = true
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
                birthScale0: embed = ValueVector3 {
                    constantValue: vec3 = { 15, 15, 15 }
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
                            { 15, 15, 15 }
                        }
                    }
                }
                scale0: embed = ValueVector3 {
                    dynamics: pointer = VfxAnimatedVector3fVariableData {
                        times: list[f32] = {
                            0
                            0.400000006
                            0.600000024
                            1
                        }
                        values: list[vec3] = {
                            { 0.5, 0.5, 0.5 }
                            { 2, 2, 2 }
                            { 2, 2, 2 }
                            { 1, 1, 1 }
                        }
                    }
                }
                texture: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Spirit_Phoenix_Flames.tex"
                uvMode: u8 = 2
                birthUvScrollRate: embed = ValueVector2 {
                    constantValue: vec2 = { 0.25, 0.550000012 }
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
                            { 0.25, 0.550000012 }
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
                    textureMult: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Spirit_Phoenix_Flames_Mult.tex"
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
                                        1
                                        -0.200000003
                                    }
                                }
                                VfxProbabilityTableData {
                                    keyTimes: list[f32] = {
                                        0
                                        1
                                    }
                                    keyValues: list[f32] = {
                                        1
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
        visibilityRadius: f32 = 9999999
        particleName: string = "Rell_Skin20_Idle_Body_Glow"
        particlePath: string = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Idle_Body_Glow"
    }
    "Characters/Rell/Skins/Skin20/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
            "Rell_P_Ring" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_P_Ring"
            "Rell_P_ArmorShred" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_P_ArmorShred"
            "Rell_Q_Cast" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_Cast"
            "Rell_Q_Indicator" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_Indicator"
            "Rell_Q_Stab" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_Stab"
            "Rell_Q_VFX_Mis" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_VFX_Mis"
            "Rell_Q_Tar_Child" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_Tar_Child"
            "Rell_Q_Tar" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_Tar"
            "Rell_Q_Tar_ShieldBreak" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_Tar_ShieldBreak"
            "Rell_Q_Heal" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_Heal"
            "Rell_E_Tether_Armed" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Tether_Armed"
            "Rell_E_Beam_Snap" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Beam_Snap"
            "Rell_E_Cricle_Explosion" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Cricle_Explosion"
            "Rell_E_Tether_Hit" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Tether_Hit"
            "Rell_E_Pointer" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Pointer"
            "Rell_E_Ring_Solo" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Ring_Solo"
            "Rell_E_Tether_Persist" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Tether_Persist"
            "Rell_E_tether_range_indicator" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_tether_range_indicator"
            "Rell_W_Mount_Transform" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Mount_Transform"
            "Rell_W_Dismount_AOE" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Dismount_AOE"
            "Rell_W_Dismount_Cast" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Dismount_Cast"
            "Rell_W_Dismount_AOE_Indicator_Enemy" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Dismount_AOE_Indicator_Enemy"
            "Rell_W_Dismount_Slide_Indicator_Enemy" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Dismount_Slide_Indicator_Enemy"
            "Rell_W_Dismount_Slide_AOE" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Dismount_Slide_AOE"
            "Rell_W_Tar" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Tar"
            "Rell_W_Tar_KnockUp" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Tar_KnockUp"
            0x799c2c66 = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Mount_Buf_Ground"
            "Rell_W_Shield" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Shield"
            "Rell_R_Cas_Body" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_R_Cas_Body"
            "Rell_R_tar" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_R_tar"
            "Rell_R_AOE" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_R_AOE"
            "Rell_R_Cas_AOE" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_R_Cas_AOE"
            "Rell_R_Suck_tar" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_R_Suck_tar"
            "Rell_R_Hit_Tick" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_R_Hit_Tick"
            "Rell_R_Hit_Streak" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_R_Hit_Streak"
            "Rell_R_Buf" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_R_Buf"
            "Rell_E_VFX_mis" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_VFX_mis"
            "Rell_E_Ally_Indicator_Far" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Ally_Indicator_Far"
            "Rell_E_Ally_Activate" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Ally_Activate"
            "Rell_W_Mount_Buf_Lance" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Mount_Buf_Lance"
            "Rell_W_Mount_Transform_Child" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Mount_Transform_Child"
            "Rell_W_Mount_Buf_Steam" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Mount_Buf_Steam"
            "Rell_W_Mount_Rib_Glow" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Mount_Rib_Glow"
            "Rell_BA_Swipe_Mounted" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_BA_Swipe_Mounted"
            "Rell_BA_Tar" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_BA_Tar"
            "Rell_BA_Swipe_Grounded_01" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_BA_Swipe_Grounded_01"
            "Rell_BA_Swipe_Grounded_02" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_BA_Swipe_Grounded_02"
            "Rell_E_Ally_Indicator_Near" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Ally_Indicator_Near"
            "Rell_E_Ally_Indicator_Med" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Ally_Indicator_Med"
            "Rell_Q_Stab_Child" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_Stab_Child"
            "Rell_Q_Stab_Grounded" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_Stab_Grounded"
            "Rell_Q_Stab_Child_Ground" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_Stab_Child_Ground"
            "Rell_W_Dismount_Hover" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Dismount_Hover"
            "Rell_W_Dismount_Jump" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Dismount_Jump"
            "Rell_E_Cast" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Cast"
            0x55b021f9 = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_BA_Swipe_Child"
            "Rell_BA_Swipe_Child_Spear" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_BA_Swipe_Child_Spear"
            "Rell_BA_Swipe_Child_Kick" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_BA_Swipe_Child_Kick"
            0xf5562299 = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_BA_Swipe_Grounded_Crit"
            0x982336b1 = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_BA_Swipe_Mounted_Crit"
            "Rell_W_Flip_Swipe" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Flip_Swipe"
            "Rell_Q_Heal_Child" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Q_Heal_Child"
            "Rell_E_Snap_Mis" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Snap_Mis"
            "Rell_E_Snap_Cas" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Snap_Cas"
            "Rell_E_Ring" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Ring"
            "Rell_W_Dismount_AOE_Indicator_Friendly" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Dismount_AOE_Indicator_Friendly"
            "Rell_W_Dismount_Slide_Indicator_Friendly" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Dismount_Slide_Indicator_Friendly"
            "Rell_Emote_Death_Dust_Horse" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Emote_Death_Dust_Horse"
            "Rell_Emote_Death_Dust_Lance" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Emote_Death_Dust_Lance"
            "Rell_Emote_Death_Dust_Rell" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Emote_Death_Dust_Rell"
            "Rell_Emote_Dance_Dust_Hoofprints" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Emote_Dance_Dust_Hoofprints"
            "Rell_Emote_Dance_Lance_Stab" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Emote_Dance_Lance_Stab"
            "Rell_Emote_Dance_R_Hoofprints" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Emote_Dance_R_Hoofprints"
            "Rell_Emote_Recall_Winddown" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Emote_Recall_Winddown"
            "Rell_Emote_Recall_Winddown_Steam" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Emote_Recall_Winddown_Steam"
            "Rell_Emote_Recall_Winddown_Dust_Blow" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Emote_Recall_Winddown_Dust_Blow"
            "Rell_Emote_Recall_Chroma_Lance" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Emote_Recall_Chroma_Lance"
            "Rell_Emote_Recall_Lance_Stab" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Emote_Recall_Lance_Stab"
            "Rell_P_ArmorShred_Minion" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_P_ArmorShred_Minion"
            "Rell_E_buff" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_buff"
            "Rell_E_Stage2" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Stage2"
            "Rell_E_Stage3" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Stage3"
            0xce7eb5a8 = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_SlowField"
            "Rell_E_Empowered_Lance" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_E_Empowered_Lance"
            "Rell_P_ArmorShred2" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_P_ArmorShred2"
            "Rell_P_ArmorShred3" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_P_ArmorShred3"
            "Rell_P_ArmorShred4" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_P_ArmorShred4"
            "Rell_P_ArmorShred5" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_P_ArmorShred5"
            "Rell_P_ArmorShred_Minion2" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_P_ArmorShred_Minion2"
            "Rell_P_ArmorShred_Minion3" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_P_ArmorShred_Minion3"
            "Rell_P_ArmorShred_Minion4" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_P_ArmorShred_Minion4"
            "Rell_P_ArmorShred_Minion5" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_P_ArmorShred_Minion5"
            "Rell_W_Ally_Buf_Ground" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_W_Ally_Buf_Ground"
            0x65ee4617 = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_BA_Tar01"
            0xb23c8936 = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_BA_Tar01"
            0xd7e05705 = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_globalhit_physical"
            "Rell_BA_Tar01" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_BA_Tar01"
            "Rell_Idle_Body_Glow" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Idle_Body_Glow"
            "Rell_Idle_Body_Glow1" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Idle_Body_Glow1"
            "Rell_R_Tumbleweed_Child" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_R_Tumbleweed_Child"
            0xdae9a9ef = "Characters/Rell/Skins/Skin20/Particles/Rell_Base_R_Tumbleweed_Child03"
            "Rell_R_Tumbleweed_Child03" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_R_Tumbleweed_Child03"
            "Rell_R_Tumbleweed_Child04" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_R_Tumbleweed_Child04"
            0xa5bdcff1 = 0x00000000
            "Rell_Reacll_trail_01" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Reacll_trail_01"
            "Rell_RecallFissure" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_RecallFissure"
            "Rell_Reacll_Absorb" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Reacll_Absorb"
            "Rell_Landing_Child" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Landing_Child"
            "Rell_Reacll_Absorb_Child" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Reacll_Absorb_Child"
            0x02ea7514 = 0x00000000
            "Rell_Recall_Tar_Child" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Recall_Tar_Child"
            "Rell_Reacll_trail_02" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Reacll_trail_02"
            "Rell_Recall_Mouse" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Recall_Mouse"
            "Rell_Recall_Prick" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Recall_Prick"
            "Rell_Recall_Prick_Child" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Recall_Prick_Child"
            "Rell_Recall_Cone" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Recall_Cone"
            "Rell_Recall_Tar_Child2" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Recall_Tar_Child2"
            "Rell_Recall_Tar2" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Recall_Tar2"
            "Rell_Recall_Ground" = "Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Recall_Ground"
        }
    }
    "Characters/Rell/Skins/Skin20/Materials/Rell_Horse_VFX" = StaticMaterialDef {
        name: string = "Characters/Rell/Skins/Skin20/Materials/Rell_Horse_VFX"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "Diffuse_Texture"
                texturePath: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Darkstar_Lava.tex"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Mask_Texture"
                texturePath: string = "ASSETS/Characters/Rell/Skins/Skin20/Particles/Rell_Skin20_Horse_Noise.tex"
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Additive_Intensity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Noise_Scale"
                value: vec4 = { 3, 1, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Scroll_Speed"
                value: vec4 = { -0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Addative_Color"
                value: vec4 = { 1, 0.321568638, 0.00784313772, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 4, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_color"
                value: vec4 = { 1, 0.219607845, 0.0274509806, 1 }
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
        dynamicMaterial: pointer = DynamicMaterialDef {}
    }
    "Characters/Rell/Skins/Skin20/Materials/Rell_LanceMental" = StaticMaterialDef {
        name: string = "Characters/Rell/Skins/Skin20/Materials/Rell_LanceMental"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "Diffuse_Texture"
                texturePath: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_Lance_TX_CM.tex"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Mask_Texture"
                texturePath: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Lance_TX_Mask.tex"
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Additive_Intensity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Noise_Scale"
                value: vec4 = { 3, 3, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Scroll_Speed"
                value: vec4 = { 0.0500000007, -0.5, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Addative_Color"
                value: vec4 = { 1, 0.0358281843, 0, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_Intensity"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Bloom_color"
                value: vec4 = { 1, 0.219607845, 0.0274509806, 1 }
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
        dynamicMaterial: pointer = DynamicMaterialDef {
            parameters: list[embed] = {
                DynamicMaterialParameterDef {
                    name: string = "Addative_Color"
                    enabled: bool = false
                    driver: pointer = ColorGraphMaterialDriver {
                        driver: pointer = SineMaterialDriver {
                            mDriver: pointer = TimeMaterialDriver {}
                            mFrequency: f32 = 2
                            mScale: f32 = 0.5
                        }
                        colors: embed = VfxAnimatedColorVariableData {
                            times: list[f32] = {
                                0
                                0.50333333
                                0.991666675
                            }
                            values: list[vec4] = {
                                { 1, 0.294117659, 0.0588235296, 1 }
                                { 0.180392161, 0, 0, 1 }
                                { 1, 0.294117659, 0.0588235296, 1 }
                            }
                        }
                    }
                }
            }
        }
    }
    "Characters/Rell/Skins/Skin20/Materials/Specular_Fresnel_Masked_inst" = StaticMaterialDef {
        name: string = "Characters/Rell/Skins/Skin20/Materials/Specular_Fresnel_Masked_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "Diffuse_Color"
                texturePath: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_TX_CM.tex"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Mask"
                texturePath: string = "ASSETS/Characters/Rell/Skins/Skin20/Rell_Skin20_Mask_TX_CM.tex"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "iridescentTex"
                texturePath: string = "ASSETS/Shared/Materials/Default_Gradient.dds"
            }
        }
        paramValues: list2[embed] = {
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Color"
                value: vec4 = { 0.909498751, 0.134889752, 0.0905317739, 1 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Size"
                value: vec4 = { 0.5, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Shadow_Bias"
                value: vec4 = { 1, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "MaxSpec"
                value: vec4 = { 64, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "LQ_Lighting_Intensity"
            }
            StaticMaterialShaderParamDef {
                name: string = "RimLightOffset"
                value: vec4 = { -0.419999987, -0.419999987, -0.419999987, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "SpecularColor"
                value: vec4 = { 0.886274517, 0.909803927, 1, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "IridescentControl"
                value: vec4 = { 1, 0.5, 0.5, 0 }
            }
        }
        switches: list2[embed] = {
            StaticMaterialSwitchDef {
                name: string = "IRIDESCENCE_ON"
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
                        shader: link = "Shaders/SkinnedMesh/Specular_Fresnel_Masked"
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
