#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {
    "DATA/Characters/Chogath/Chogath.bin"
    "DATA/Characters/Chogath/Animations/Skin0.bin"
    "DATA/Chogath_Skins_Root_Skins_Skin0_Skins_Skin1_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin20_Skins_Skin21_Skins_Skin22_Skins_Skin23_Skins_Skin24_Skins_Skin25_Skins_Skin26_Skins_Skin27_Skins_Skin28_Skins_Skin29_Skins_Skin3_Skins_Skin30_Skins_Skin31_Skins_Skin32_Skins_Skin33_Skins_Skin34_Skins_Skin35_Skins_Skin36_Skins_Skin37_Skins_Skin38_Skins_Skin39_Skins_Skin4_Skins_Skin40_Skins_Skin6_Skins_Skin7.bin"
    "DATA/Chogath_Skins_Skin14_Skins_Skin15_Skins_Skin16_Skins_Skin17_Skins_Skin18_Skins_Skin19_Skins_Skin20_Skins_Skin21_Skins_Skin22.bin"
}
entries: map[hash,embed] = {
    "Characters/Chogath/Skins/Skin14" = SkinCharacterDataProperties {
        skinClassification: u32 = 1
        championSkinName: string = "ChogathSkin14"
        metaDataTags: string = "faction:void,gender:male,race:monster,skinline:shanhaiscrolls"
        loadscreen: embed = CensoredImage {
            image: string = "ASSETS/Characters/Chogath/skins/Skin14/ChogathLoadscreen_14.tex"
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
    "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_W_cas" = VfxSystemDefinitionData {
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
                        material: link = "Characters/Chogath/Skins/Skin14/Materials/ChoGath_Skin14_FlowMap_Bloom_inst"
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
        particleName: string = "Chogath_Skin14_W_cas"
        particlePath: string = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_W_cas"
    }
    "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Recall_MountainMat_danshan" = VfxSystemDefinitionData {
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
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_Recall_green_TX_CM.tex"
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
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_Recall_green_TX_CM.tex"
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
        particleName: string = "Chogath_Skin14_Recall_MountainMat_danshan"
        particlePath: string = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Recall_MountainMat_danshan"
        overrideScaleCap: option[f32] = {
            200
        }
    }
    "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Emote_Recall_Outline" = VfxSystemDefinitionData {
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
                        material: link = "Characters/Chogath/Skins/Skin14/Materials/Ink_Body_inst"
                    }
                }
            }
        }
        particleName: string = "Chogath_Skin14_Emote_Recall_Outline"
        particlePath: string = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Emote_Recall_Outline"
        flags: u16 = 134
    }
    "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Idle_clould3" = VfxSystemDefinitionData {
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
                    constantValue: vec4 = { 1, 0, 0, 1 }
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
                texture: string = "ASSETS/Characters/Chogath/skins/Skin14/Particles/Chogath_Skin14_Idle_jianbian_8wei6.tex"
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
                    constantValue: vec4 = { 0.145098045, 0.0588235296, 0.0588235296, 1 }
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
        particleName: string = "Chogath_Skin14_Idle_clould3"
        particlePath: string = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Idle_clould3"
        flags: u16 = 198
    }
    "Characters/Chogath/Skins/Skin14/Materials/Ink_Prop_inst" = StaticMaterialDef {
        name: string = "Characters/Chogath/Skins/Skin14/Materials/Ink_Prop_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "Diffuse_Texture"
                texturePath: string = "ASSETS/Characters/Chogath/skins/Skin14/ChoGath_Skin14_Recall_TX_CM.tex"
                addressU: u32 = 1
                addressV: u32 = 1
                addressW: u32 = 1
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Swapped_Texture"
                texturePath: string = "ASSETS/Characters/Chogath/skins/Skin14/ChoGath_Skin14_Recall_TX_CM.tex"
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
    "Characters/Chogath/Skins/Skin14/Materials/ChoGath_Skin14_FlowMap_Bloom_inst" = StaticMaterialDef {
        name: string = "Characters/Chogath/Skins/Skin14/Materials/ChoGath_Skin14_FlowMap_Bloom_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "FlowMap"
                texturePath: string = "ASSETS/Characters/Chogath/skins/Skin14/Chogath_skin14_FM.tex"
            }
            StaticMaterialShaderSamplerDef {
                textureName: string = "Diffuse_Texture"
                texturePath: string = "ASSETS/Characters/Chogath/skins/Skin14/Chogath_Skin14_TX_CM.tex"
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
                value: vec4 = { 0.694117665, 0, 0, 0.20784314 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Fresnel"
                value: vec4 = { 2, 0, 0, 0 }
            }
            StaticMaterialShaderParamDef {
                name: string = "Fresnel_Color"
                value: vec4 = { 0.407843143, 0, 0.00784313772, 0 }
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
    "Characters/Chogath/Skins/Skin14/Materials/Ink_Body_inst" = StaticMaterialDef {
        name: string = "Characters/Chogath/Skins/Skin14/Materials/Ink_Body_inst"
        samplerValues: list2[embed] = {
            StaticMaterialShaderSamplerDef {
                textureName: string = "Diffuse_Texture"
                texturePath: string = "ASSETS/Characters/Chogath/skins/Skin14/Chogath_Skin14_TX_CM.tex"
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
    "Characters/Chogath/Skins/Skin14/Resources" = ResourceResolver {
        resourceMap: map[hash,link] = {
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
            "Chogath_W_cas" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_W_cas"
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
            "Chogath_Idle_clould3" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Idle_clould3"
            "Chogath_Idle_clould4" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Idle_clould4"
            "Chogath_Idle_bei_1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Idle_bei_1"
            "Chogath_Idle_wei" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Idle_wei"
            "Chogath_W_cas_child_2" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_W_cas_child_2"
            "Chogath_W_cas_child_3" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_W_cas_child_3"
            "Chogath_Recall_zui" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Recall_zui"
            "Chogath_Recall_MountainMat_1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Recall_MountainMat_1"
            "Chogath_Recall_MountainMat_2" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Recall_MountainMat_2"
            "Chogath_Recall_MountainMat_danshan" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Recall_MountainMat_danshan"
            "Chogath_R_tar_1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_R_tar_1"
            "Chogath_Recall_ri" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Recall_ri"
            "Chogath_R_tar_Child1_1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_R_tar_Child1_1"
            "Chogath_Recall_zui_1" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Recall_zui_1"
            "Chogath_E_Cas" = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_E_Cas"
            0x92877c7c = "Characters/Chogath/Skins/Skin14/Particles/Chogath_Skin14_Emote_Recall_Outline"
        }
    }
}
