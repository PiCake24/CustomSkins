#PROP_text
type: string = "PROP"
version: u32 = 3
linked: list[string] = {}
entries: map[hash,embed] = {
    "Characters/Sion/Animations/Skin0" = animationGraphData {
        mCascadeBlendValue: f32 = 0
        mClipDataMap: map[hash,pointer] = {
            "Crit" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Crit.anm"
                }
            }
            "death" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "WeaponHide" = SubmeshVisibilityEventData {
                        mName: hash = "WeaponHide"
                        mHideSubmeshList: list[hash] = {
                            "weapon"
                        }
                    }
                    "Audio_Death" = ParticleEventData {
                        mName: hash = "Audio_Death"
                        mEffectKey: hash = "Sion_emote_death_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Death.anm"
                }
            }
            "Joke" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "WeaponSnap" = JointSnapEventData {
                        mName: hash = "WeaponSnap"
                        mJointNameToOverride: hash = "weapon"
                        mJointNameToSnapTo: hash = "Snap_Weapon2World"
                    }
                    0xeed2417d = ParticleEventData {
                        mName: hash = 0xeed2417d
                        mEffectKey: hash = "Sion_emote_joke_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                }
                mTickDuration: f32 = 0.0333333388
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Joke.anm"
                }
            }
            "Spell1" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Attack1.anm"
                }
            }
            "Spell3" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Spell3.anm"
                }
            }
            "taunt" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "Audio_Taunt" = ParticleEventData {
                        mName: hash = "Audio_Taunt"
                        mEffectKey: hash = "Sion_emote_taunt_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Taunt.anm"
                }
            }
            "Attack2" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "trail2" = ParticleEventData {
                        mName: hash = "trail2"
                        mStartFrame: f32 = 8
                        mEffectKey: hash = "Sion_BA_trail2"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Attack2.anm"
                }
            }
            0x0e2d9deb = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xf3ae1861 = SoundEventData {
                        mName: hash = 0xf3ae1861
                        mStartFrame: f32 = 19
                        mSoundName: string = "Play_sfx_Sion_SionR_bigfoot"
                        mIsKillEvent: bool = false
                    }
                    0xf0ae13a8 = SoundEventData {
                        mName: hash = 0xf0ae13a8
                        mStartFrame: f32 = 50
                        mSoundName: string = "Play_sfx_Sion_SionR_bigfoot"
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Spell4_Run.anm"
                }
            }
            "Run" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Run.anm"
                }
            }
            "Attack1" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "trail1" = ParticleEventData {
                        mName: hash = "trail1"
                        mStartFrame: f32 = 7
                        mEffectKey: hash = "Sion_BA_trail1"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Attack1.anm"
                }
            }
            "Idle1_Base" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Idle1.anm"
                }
            }
            "Spell1_Chrg" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Spell1_CHRG.anm"
                }
            }
            "Passive_Attack1" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "WeaponHide" = SubmeshVisibilityEventData {
                        mName: hash = "WeaponHide"
                        mHideSubmeshList: list[hash] = {
                            "weapon"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Passive_Attack1.anm"
                }
            }
            "Passive_Attack2" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "HideWeapon" = SubmeshVisibilityEventData {
                        mName: hash = "HideWeapon"
                        mHideSubmeshList: list[hash] = {
                            "weapon"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Passive_Attack2.anm"
                }
            }
            "Passive_Idle1" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "weapon" = SubmeshVisibilityEventData {
                        mName: hash = "weapon"
                        mHideSubmeshList: list[hash] = {
                            "weapon"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Passive_Idle1.anm"
                }
            }
            0x7ff7bfcd = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "WeaponHide" = SubmeshVisibilityEventData {
                        mName: hash = "WeaponHide"
                        mHideSubmeshList: list[hash] = {
                            "weapon"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Passive_Run.anm"
                }
            }
            "Spell1_Hit1" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Spell1_Hit1.anm"
                }
            }
            "Spell1_Hit2" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Spell1_Hit2.anm"
                }
            }
            "Idle_In" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Idle_IN.anm"
                }
            }
            "Attack3" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "trail3" = ParticleEventData {
                        mName: hash = "trail3"
                        mStartFrame: f32 = 7
                        mEffectKey: hash = "Sion_BA_trail3"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Attack3.anm"
                }
            }
            "Run_Fast" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Run_Fast.anm"
                }
            }
            "Attack_Tower" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Attack_Tower.anm"
                }
            }
            "Run_Haste" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Run_Haste.anm"
                }
            }
            "Passive_Death" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "JointSnap" = JointSnapEventData {
                        mName: hash = "JointSnap"
                        mStartFrame: f32 = 12
                        mJointNameToOverride: hash = "weapon"
                        mJointNameToSnapTo: hash = "Snap_Weapon2World"
                    }
                    0xd277d8fb = ParticleEventData {
                        mName: hash = 0xd277d8fb
                        mStartFrame: f32 = 20
                        mEffectKey: hash = "Sion_Passive_Ax"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0x8a573651 = SubmeshVisibilityEventData {
                        mName: hash = 0x8a573651
                        mStartFrame: f32 = 23
                        mHideSubmeshList: list[hash] = {
                            "weapon"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Passive_Death.anm"
                }
            }
            "Channel" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_channel_loop.anm"
                }
            }
            "Channel_Wndup" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_channel_in.anm"
                }
            }
            "Stunned" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Stunned.anm"
                }
            }
            0xa09e88b7 = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "WeaponHide" = SubmeshVisibilityEventData {
                        mName: hash = "WeaponHide"
                        mHideSubmeshList: list[hash] = {
                            "weapon"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Passive_Run_In.anm"
                }
            }
            "Passive_Run" = SequencerClipData {
                mClipNameList: list[hash] = {
                    0xa09e88b7
                    0x7ff7bfcd
                }
            }
            "Laugh" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xc09e7515 = ParticleEventData {
                        mName: hash = 0xc09e7515
                        mEffectKey: hash = "Sion_Emote_Laugh"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "c_buffbone_glb_head_loc"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                    0x0cf0606b = ParticleEventData {
                        mName: hash = 0x0cf0606b
                        mEffectKey: hash = "Sion_emote_laugh_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Laugh.anm"
                }
            }
            0xbb7b9f71 = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_KnockedUp.anm"
                }
            }
            "Passive_Dash" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "WeaponHide" = SubmeshVisibilityEventData {
                        mName: hash = "WeaponHide"
                        mHideSubmeshList: list[hash] = {
                            "weapon"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Passive_Dash.anm"
                }
            }
            "Recall" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "JointSnap" = JointSnapEventData {
                        mName: hash = "JointSnap"
                        mStartFrame: f32 = 17
                        mJointNameToOverride: hash = "weapon"
                        mJointNameToSnapTo: hash = "Snap_Weapon2World"
                    }
                    "Audio_Recall" = ParticleEventData {
                        mName: hash = "Audio_Recall"
                        mEffectKey: hash = "Sion_recall_start_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Recall.anm"
                }
            }
            "Spell4" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Spell4_Hit.anm"
                }
            }
            "Spell4_Hit" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Spell4_Hit.anm"
                }
            }
            "Attack_Tower2" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "trail4" = ParticleEventData {
                        mName: hash = "trail4"
                        mStartFrame: f32 = 7
                        mEffectKey: hash = "Sion_BA_trail4"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {
                                mBoneName: hash = "C_Buffbone_GLB_Layout_Loc"
                            }
                        }
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Attack2_Tower.anm"
                }
            }
            "Spell4_RunIn" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xa1fe712e = SoundEventData {
                        mName: hash = 0xa1fe712e
                        mStartFrame: f32 = 19
                        mSoundName: string = "Play_sfx_Sion_SionR_smallfoot"
                        mIsKillEvent: bool = false
                    }
                    0xa0fe6f9b = SoundEventData {
                        mName: hash = 0xa0fe6f9b
                        mStartFrame: f32 = 50
                        mSoundName: string = "Play_sfx_Sion_SionR_smallfoot"
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Spell4_RunIN.anm"
                }
            }
            "Dance_Loop" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "WeaponSnap" = JointSnapEventData {
                        mName: hash = "WeaponSnap"
                        mJointNameToOverride: hash = "weapon"
                        mJointNameToSnapTo: hash = "Snap_Weapon2World"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Dance_LOOP.anm"
                }
            }
            "Dance_In" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "WeaponSnap" = JointSnapEventData {
                        mName: hash = "WeaponSnap"
                        mStartFrame: f32 = 9
                        mJointNameToOverride: hash = "weapon"
                        mJointNameToSnapTo: hash = "Snap_Weapon2World"
                    }
                    0xddf80471 = ParticleEventData {
                        mName: hash = 0xddf80471
                        mEffectKey: hash = "Sion_emote_dance_in_sound"
                        mParticleEventDataPairList: list[embed] = {
                            ParticleEventDataPair {}
                        }
                        mIsLoop: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Dance_IN.anm"
                }
            }
            "Dance" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Dance_In"
                    0x9733b790
                }
            }
            "Spell4_Run" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Spell4_RunIn"
                    "Spell4_RunIn"
                    0x0e2d9deb
                }
            }
            "Idle2_Base" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Idle2.anm"
                }
            }
            0x9733b790 = SequencerClipData {
                mFlags: u32 = 2
                mClipNameList: list[hash] = {
                    "Dance_Loop"
                    "Dance_Loop"
                    "Dance_Spin"
                }
            }
            "Dance_Spin" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "WeaponSnap" = JointSnapEventData {
                        mName: hash = "WeaponSnap"
                        mJointNameToOverride: hash = "weapon"
                        mJointNameToSnapTo: hash = "Snap_Weapon2World"
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Dance_SPIN.anm"
                }
            }
            "Spell4_Stop" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    0xfaea3767 = SoundEventData {
                        mName: hash = 0xfaea3767
                        mSoundName: string = "Play_sfx_Sion_SionR_onjump"
                        mIsLoop: bool = false
                        mIsKillEvent: bool = false
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Spell4_STOP.anm"
                }
            }
            "Run_Slow" = AtomicClipData {
                mFlags: u32 = 2
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Run_Slow.anm"
                }
            }
            "KnockedUp_In" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_KnockedUp_IN.anm"
                }
            }
            "KnockedUp" = SequencerClipData {
                mClipNameList: list[hash] = {
                    "KnockedUp_In"
                    0xbb7b9f71
                }
            }
            "Idle1" = SelectorClipData {
                mSelectorPairDataList: list[embed] = {
                    SelectorPairData {
                        mClipName: hash = "Idle1_Base"
                        mProbability: f32 = 95
                    }
                    SelectorPairData {
                        mClipName: hash = "Idle2_Base"
                        mProbability: f32 = 5
                    }
                }
            }
            0xf721651e = SequencerClipData {
                mClipNameList: list[hash] = {
                    "Passive_Dance_IN"
                    0x1c772fea
                }
            }
            "Passive_Dance_IN" = AtomicClipData {
                mFlags: u32 = 8
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "WeaponHide" = SubmeshVisibilityEventData {
                        mName: hash = "WeaponHide"
                        mHideSubmeshList: list[hash] = {
                            "weapon"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Dance_IN.anm"
                }
            }
            0x2469b82f = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "WeaponHide" = SubmeshVisibilityEventData {
                        mName: hash = "WeaponHide"
                        mHideSubmeshList: list[hash] = {
                            "weapon"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Dance_SPIN.anm"
                }
            }
            "Passive_Dance_LOOP" = AtomicClipData {
                mTrackDataName: hash = "Default"
                mEventDataMap: map[hash,pointer] = {
                    "WeaponHide" = SubmeshVisibilityEventData {
                        mName: hash = "WeaponHide"
                        mHideSubmeshList: list[hash] = {
                            "weapon"
                        }
                    }
                }
                mAnimationResourceData: embed = AnimationResourceData {
                    mAnimationFilePath: string = "ASSETS/Characters/Sion/Skins/Base/Animations/Sion_Dance_LOOP.anm"
                }
            }
            0x1c772fea = SequencerClipData {
                mFlags: u32 = 2
                mClipNameList: list[hash] = {
                    "Passive_Dance_LOOP"
                    "Passive_Dance_LOOP"
                    0x2469b82f
                }
            }
        }
        mMaskDataMap: map[hash,embed] = {
            0x445d2f1c = MaskData {
                mWeightList: list[f32] = {
                    0
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    0
                    1
                    1
                    0
                    1
                    0
                    0
                    0
                    1
                    0
                    1
                    0
                    1
                    0
                    0
                    1
                    1
                    1
                    1
                    1
                    0
                    0
                    0
                    0
                    0
                }
            }
        }
        mTrackDataMap: map[hash,embed] = {
            0x3b54abe0 = TrackData {}
            "Default" = TrackData {
                mPriority: u8 = 1
            }
        }
        mBlendDataTable: map[u64,pointer] = {
            597025090215415592 = TimeBlendData {
                mTime: f32 = 0
            }
            597025090609833815 = TimeBlendData {
                mTime: f32 = 0
            }
            597025091218182896 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            597025093162778695 = TimeBlendData {
                mTime: f32 = 0
            }
            597025093296196313 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            597025094000270714 = TimeBlendData {
                mTime: f32 = 0
            }
            690925388999076091 = TimeBlendData {
                mTime: f32 = 0
            }
            690925389371631447 = TimeBlendData {
                mTime: f32 = 0
            }
            690925389979980528 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            690925391924576327 = TimeBlendData {
                mTime: f32 = 0
            }
            690925392057993945 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            690925392233291277 = TimeBlendData {
                mTime: f32 = 0
            }
            690925392762068346 = TimeBlendData {
                mTime: f32 = 0
            }
            762984713925601934 = TimeBlendData {
                mTime: f32 = 0
            }
            762984714281379671 = TimeBlendData {
                mTime: f32 = 0
            }
            762984714889728752 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            762984716834324551 = TimeBlendData {
                mTime: f32 = 0
            }
            762984716967742169 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            762984717143039501 = TimeBlendData {
                mTime: f32 = 0
            }
            762984717671816570 = TimeBlendData {
                mTime: f32 = 0
            }
            1021646323363716587 = TimeBlendData {
                mTime: f32 = 0
            }
            1021646323659269975 = TimeBlendData {
                mTime: f32 = 0
            }
            1021646324267619056 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            1021646326212214855 = TimeBlendData {
                mTime: f32 = 0
            }
            1021646326345632473 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            1021646326520929805 = TimeBlendData {
                mTime: f32 = 0
            }
            1021646327049706874 = TimeBlendData {
                mTime: f32 = 0
            }
            2291038459341268823 = TimeBlendData {
                mTime: f32 = 0
            }
            2291038459949617904 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2291038462027631321 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            2291038462731705722 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597613595027287 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597613627986596 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597614203376368 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2432597616147972167 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597616281389785 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            2432597616456687117 = TimeBlendData {
                mTime: f32 = 0
            }
            2432597616985464186 = TimeBlendData {
                mTime: f32 = 0
            }
            2786235694510204759 = TimeBlendData {
                mTime: f32 = 0
            }
            2786235694625501850 = TimeBlendData {
                mTime: f32 = 0
            }
            2786235695118553840 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            2786235695791550182 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            2786235697063149639 = TimeBlendData {
                mTime: f32 = 0
            }
            2786235697196567257 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            2786235697371864589 = TimeBlendData {
                mTime: f32 = 0
            }
            2786235697900641658 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207949842442071 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207950027116234 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207950450791152 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            3084207951123787494 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            3084207952395386951 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207952528804569 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            3084207952704101901 = TimeBlendData {
                mTime: f32 = 0
            }
            3084207953232878970 = TimeBlendData {
                mTime: f32 = 0
            }
            4242333434393618263 = TimeBlendData {
                mTime: f32 = 0
            }
            4242333434847939528 = TimeBlendData {
                mTime: f32 = 0
            }
            4242333435001967344 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4242333436946563143 = TimeBlendData {
                mTime: f32 = 0
            }
            4242333437079980761 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            4242333437255278093 = TimeBlendData {
                mTime: f32 = 0
            }
            4242333437784055162 = TimeBlendData {
                mTime: f32 = 0
            }
            4880364432276393768 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364432298256635 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364432315034254 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364432375258603 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364432670811991 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364432703771300 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364432786109082 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364432855486154 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364433125133256 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364433273686424 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364433279161072 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364433324019281 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364433339781607 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364433591888164 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364433625443402 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364433642221021 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364433655840176 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364433669614991 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364433871463955 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364433876463780 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364433952157414 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            4880364434259504085 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364434284330957 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364434659476877 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364434832132279 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364434892178189 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364434938559449 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364435139868776 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364435173424014 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364435216094491 = TimeBlendData {
                mTime: f32 = 0.400000006
            }
            4880364435223756871 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364435238524790 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364435282829169 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364435301762147 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364435310951757 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364435357174489 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364435532471821 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364435620033302 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364435738936819 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364435893577265 = TimeBlendData {
                mTime: f32 = 0.699999988
            }
            4880364436061248890 = TimeBlendData {
                mTime: f32 = 0
            }
            4903877867396272880 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            4903877868069269222 = TimeBlendData {
                mTime: f32 = 1
            }
            4903877869333206299 = TimeBlendData {
                mTime: f32 = 1
            }
            4903877869340868679 = TimeBlendData {
                mTime: f32 = 0
            }
            4903877869474286297 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            4903877869649583629 = TimeBlendData {
                mTime: f32 = 0
            }
            5096542408681402086 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            5096542410040196429 = TimeBlendData {}
            5164241082078947159 = TimeBlendData {
                mTime: f32 = 0
            }
            5164241082687296240 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            5164241082747916775 = TimeBlendData {
                mTime: f32 = 0
            }
            5164241084631892039 = TimeBlendData {
                mTime: f32 = 0
            }
            5164241084765309657 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            5164241084940606989 = TimeBlendData {
                mTime: f32 = 0
            }
            5164241085469384058 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030499501107031 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030500109456112 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6247030500422183204 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030500782452454 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            6247030502054051911 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030502187469529 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            6247030502362766861 = TimeBlendData {
                mTime: f32 = 0
            }
            6247030502891543930 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149149320603479 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149149928952560 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6391149150275234890 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149150601948902 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            6391149151873548359 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149152006965977 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            6391149152182263309 = TimeBlendData {
                mTime: f32 = 0
            }
            6391149152711040378 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208474230351703 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208474838700784 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6463208475201760733 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208475511697126 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            6463208476219016589 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6463208476699408488 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208476732963726 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208476783296583 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208476870491469 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208476916714201 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            6463208477092011533 = TimeBlendData {
                mTime: f32 = 0
            }
            6463208477620788602 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702299554506583 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702300162855664 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6521702300539534768 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702302107451463 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702302240869081 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            6521702302416166413 = TimeBlendData {
                mTime: f32 = 0
            }
            6521702302944943482 = TimeBlendData {
                mTime: f32 = 0
            }
            6580864679487956823 = TimeBlendData {
                mTime: f32 = 0
            }
            6580864680096305904 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            6580864680486759823 = TimeBlendData {
                mTime: f32 = 0
            }
            6580864682040901703 = TimeBlendData {
                mTime: f32 = 0
            }
            6580864682174319321 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            6580864682349616653 = TimeBlendData {
                mTime: f32 = 0
            }
            6580864682878393722 = TimeBlendData {
                mTime: f32 = 0
            }
            7447799378599438167 = TimeBlendData {
                mTime: f32 = 0
            }
            7447799379207787248 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7447799379800090131 = TimeBlendData {
                mTime: f32 = 0
            }
            7447799379880783590 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            7447799381152383047 = TimeBlendData {
                mTime: f32 = 0
            }
            7447799381285800665 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            7447799381461097997 = TimeBlendData {
                mTime: f32 = 0
            }
            7447799381989875066 = TimeBlendData {
                mTime: f32 = 0
            }
            7469273463460161367 = TimeBlendData {
                mTime: f32 = 0
            }
            7469273464068510448 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7469273464665813156 = TimeBlendData {
                mTime: f32 = 0
            }
            7469273466013106247 = TimeBlendData {
                mTime: f32 = 0
            }
            7469273466146523865 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            7469273466321821197 = TimeBlendData {
                mTime: f32 = 0
            }
            7469273466850598266 = TimeBlendData {
                mTime: f32 = 0
            }
            7794375146005555031 = TimeBlendData {
                mTime: f32 = 0
            }
            7794375146613904112 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            7794375147286900454 = TimeBlendData {
                mTime: f32 = 0
            }
            7794375148558499911 = TimeBlendData {
                mTime: f32 = 0
            }
            7794375148691917529 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            7794375148867214861 = TimeBlendData {
                mTime: f32 = 0
            }
            7794375149395991930 = TimeBlendData {
                mTime: f32 = 0
            }
            9114419047093375728 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            9114419048073718741 = TimeBlendData {
                mTime: f32 = 0
            }
            9114419049171389145 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            9221049649787004759 = TimeBlendData {
                mTime: f32 = 0
            }
            9221049650395353840 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            9221049651400523725 = TimeBlendData {
                mTime: f32 = 0
            }
            9221049652339949639 = TimeBlendData {
                mTime: f32 = 0
            }
            9221049652473367257 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            9221049652648664589 = TimeBlendData {
                mTime: f32 = 0
            }
            9221049653177441658 = TimeBlendData {
                mTime: f32 = 0
            }
            9834587782771341691 = TimeBlendData {
                mTime: f32 = 0
            }
            9834587783626989425 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289107414837079 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289108023186160 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10832289109403501965 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            10832289109883893864 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289109917449102 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289109967781959 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289110054976845 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289110101199577 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            10832289110276496909 = TimeBlendData {
                mTime: f32 = 0
            }
            10832289110805273978 = TimeBlendData {
                mTime: f32 = 0
            }
            10895253755179284368 = TimeBlendData {
                mTime: f32 = 0
            }
            11294130477607997396 = TimeBlendData {
                mTime: f32 = 0
            }
            11573838412482570071 = TimeBlendData {
                mTime: f32 = 0
            }
            11573838413090919152 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11573838414643890359 = TimeBlendData {
                mTime: f32 = 0
            }
            11573838415035514951 = TimeBlendData {
                mTime: f32 = 0
            }
            11573838415168932569 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            11573838415344229901 = TimeBlendData {
                mTime: f32 = 0
            }
            11573838415873006970 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733632191129431 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733632799478512 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            11831733634412495629 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634744074311 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733634877491929 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            11831733635052789261 = TimeBlendData {
                mTime: f32 = 0
            }
            11831733635581566330 = TimeBlendData {
                mTime: f32 = 0
            }
            12030939627038402391 = TimeBlendData {
                mTime: f32 = 0
            }
            12030939627646751472 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12030939628319747814 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            12030939629306149849 = TimeBlendData {
                mTime: f32 = 0
            }
            12030939629591347271 = TimeBlendData {
                mTime: f32 = 0
            }
            12030939629724764889 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            12030939629900062221 = TimeBlendData {
                mTime: f32 = 0
            }
            12030939630428839290 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556602883172183 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556603491521264 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            12895556603854581213 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            12895556604871837069 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            12895556605352228968 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            12895556605385784206 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            12895556605436117063 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556605514122339 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            12895556605523311949 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556605569534681 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            12895556605606507590 = TimeBlendData {
                mTime: f32 = 0.300000012
            }
            12895556605744832013 = TimeBlendData {
                mTime: f32 = 0
            }
            12895556606273609082 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675252702668631 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675253311017712 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13039675253984014054 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            13039675254691333517 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13039675255171725416 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675255205280654 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675255255613511 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675255342808397 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675255389031129 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            13039675255564328461 = TimeBlendData {
                mTime: f32 = 0
            }
            13039675256093105530 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647003382048599 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647003990397680 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13156647005911895230 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647005934993479 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647006068411097 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            13156647006243708429 = TimeBlendData {
                mTime: f32 = 0
            }
            13156647006772485498 = TimeBlendData {
                mTime: f32 = 0
            }
            13222943555922388823 = TimeBlendData {
                mTime: f32 = 0
            }
            13222943556530737904 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13222943557203734246 = TimeBlendData {
                mTime: f32 = 0
            }
            13222943558467671323 = TimeBlendData {
                mTime: f32 = 0
            }
            13222943558475333703 = TimeBlendData {
                mTime: f32 = 0
            }
            13222943558608751321 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            13222943558784048653 = TimeBlendData {
                mTime: f32 = 0
            }
            13222943559312825722 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853227431913303 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853228040262384 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13255853229984858183 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853230118275801 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            13255853230293573133 = TimeBlendData {
                mTime: f32 = 0
            }
            13255853230822350202 = TimeBlendData {
                mTime: f32 = 0
            }
            13319280956271336939 = TimeBlendData {
                mTime: f32 = 0.400000006
            }
            13319280956566890327 = TimeBlendData {
                mTime: f32 = 0
            }
            13319280957175239408 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13319280959134603126 = TimeBlendData {
                mTime: f32 = 0
            }
            13319280959253252825 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            13319280959957327226 = TimeBlendData {
                mTime: f32 = 0
            }
            13509566815441479511 = TimeBlendData {
                mTime: f32 = 0
            }
            13509566816049828592 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13509566817994424391 = TimeBlendData {
                mTime: f32 = 0
            }
            13509566818053496689 = TimeBlendData {
                mTime: f32 = 0
            }
            13509566818127842009 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            13509566818303139341 = TimeBlendData {
                mTime: f32 = 0
            }
            13509566818831916410 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883336767366999 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883337375716080 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13590883338756031885 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13590883339236423784 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339269979022 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339320311879 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339398317155 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339407506765 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883339453729497 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            13590883339629026829 = TimeBlendData {
                mTime: f32 = 0
            }
            13590883340157803898 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352411180361559 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352411788710640 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13630352413169026445 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13630352413649418344 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413682973582 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413733306439 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413820501325 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352413866724057 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            13630352414042021389 = TimeBlendData {
                mTime: f32 = 0
            }
            13630352414570798458 = TimeBlendData {
                mTime: f32 = 0
            }
            13828877533452134231 = TimeBlendData {
                mTime: f32 = 0
            }
            13828877534055008664 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13828877534060483312 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13828877534105341521 = TimeBlendData {
                mTime: f32 = 0
            }
            13828877536005079111 = TimeBlendData {
                mTime: f32 = 0
            }
            13828877536138496729 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            13828877536313794061 = TimeBlendData {
                mTime: f32 = 0
            }
            13828877536842571130 = TimeBlendData {
                mTime: f32 = 0
            }
            13867362384444834973 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674968445118295 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674969053467376 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13987674970433783181 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            13987674970914175080 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674970947730318 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674970998063175 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674971085258061 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674971131480793 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            13987674971168453702 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674971306778125 = TimeBlendData {
                mTime: f32 = 0
            }
            13987674971835555194 = TimeBlendData {
                mTime: f32 = 0
            }
            14581773841468188503 = TimeBlendData {
                mTime: f32 = 0
            }
            14581773842076537584 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            14581773844021133383 = TimeBlendData {
                mTime: f32 = 0
            }
            14581773844154551001 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            14581773844329848333 = TimeBlendData {
                mTime: f32 = 0
            }
            14581773844858625402 = TimeBlendData {
                mTime: f32 = 0
            }
            14957847540033859302 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            14957847541438876377 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            14957847541701735190 = TimeBlendData {
                mTime: f32 = 0
            }
            15468534255646893911 = TimeBlendData {
                mTime: f32 = 0
            }
            15468534256255242992 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            15468534256928239334 = TransitionClipBlendData {
                mClipName: hash = "Idle_In"
            }
            15468534258199838791 = TimeBlendData {
                mTime: f32 = 0
            }
            15468534258333256409 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            15468534258715018739 = TimeBlendData {
                mTime: f32 = 0
            }
            15468534259037330810 = TimeBlendData {
                mTime: f32 = 0
            }
            16132709914464097008 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16132709916542110425 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            16132709917078513201 = TimeBlendData {
                mTime: f32 = 0
            }
            16852854059697923927 = TimeBlendData {
                mTime: f32 = 0
            }
            16852854060306273008 = TimeBlendData {
                mTime: f32 = 0.100000001
            }
            16852854062384286425 = TimeBlendData {
                mTime: f32 = 0.800000012
            }
            16852854063088360826 = TimeBlendData {
                mTime: f32 = 0
            }
            17876238950559197340 = TimeBlendData {
                mTime: f32 = 0
            }
        }
    }
}
