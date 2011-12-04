# // Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
# // Jad home page: http://www.kpdus.com/jad.html
# // Decompiler options: packimports(3) braces deadcode fieldsfirst 
# 
# package net.minecraft.src;
# 
# import java.io.PrintStream;
# import java.util.*;
# 
# // Referenced classes of package net.minecraft.src:
# //            Entity, MathHelper, Packet34EntityTeleport, Packet33RelEntityMoveLook, 
# //            Packet31RelEntityMove, Packet32EntityLook, Packet28EntityVelocity, DataWatcher, 
# //            Packet40EntityMetadata, EntityPlayerMP, NetServerHandler, Packet29DestroyEntity, 
# //            Packet5PlayerInventory, EntityPlayer, Packet17Sleep, EntityLiving, 
# //            PotionEffect, Packet41EntityEffect, EntityItem, Packet21PickupSpawn, 
# //            Packet20NamedEntitySpawn, EntityMinecart, Packet23VehicleSpawn, EntityBoat, 
# //            IAnimals, Packet24MobSpawn, EntityDragon, EntityFishHook, 
# //            EntityArrow, EntitySnowball, EntityPotion, EntityEnderPearl, 
# //            EntityEnderEye, EntitySmallFireball, EntityFireball, EntityEgg, 
# //            EntityTNTPrimed, EntityEnderCrystal, EntityFallingSand, Block, 
# //            EntityPainting, Packet25EntityPainting, EntityXPOrb, Packet26EntityExpOrb, 
# //            Packet
# 
# public class EntityTrackerEntry
# {
# 
#     public Entity trackedEntity;
#     public int trackingDistanceThreshold;
#     public int field_9234_e;
#     public int encodedPosX;
#     public int encodedPosY;
#     public int encodedPosZ;
#     public int encodedRotationYaw;
#     public int encodedRotationPitch;
#     public double lastTrackedEntityMotionX;
#     public double lastTrackedEntityMotionY;
#     public double lastTrackedEntityMotionZ;
#     public int updateCounter;
#     private double lastTrackedEntityPosX;
#     private double lastTrackedEntityPosY;
#     private double lastTrackedEntityPosZ;
#     private boolean firstUpdateDone;
#     private boolean shouldSendMotionUpdates;
#     private int field_28165_t;
#     public boolean playerEntitiesUpdated;
#     public Set trackedPlayers;
# 
#     public EntityTrackerEntry(Entity entity, int i, int j, boolean flag)
#     {
#         updateCounter = 0;
#         firstUpdateDone = false;
#         field_28165_t = 0;
#         playerEntitiesUpdated = false;
#         trackedPlayers = new HashSet();
#         trackedEntity = entity;
#         trackingDistanceThreshold = i;
#         field_9234_e = j;
#         shouldSendMotionUpdates = flag;
#         encodedPosX = MathHelper.floor_double(entity.posX * 32D);
#         encodedPosY = MathHelper.floor_double(entity.posY * 32D);
#         encodedPosZ = MathHelper.floor_double(entity.posZ * 32D);
#         encodedRotationYaw = MathHelper.floor_float((entity.rotationYaw * 256F) / 360F);
#         encodedRotationPitch = MathHelper.floor_float((entity.rotationPitch * 256F) / 360F);
#     }
# 
#     public boolean equals(Object obj)
#     {
#         if(obj instanceof EntityTrackerEntry)
#         {
#             return ((EntityTrackerEntry)obj).trackedEntity.entityId == trackedEntity.entityId;
#         } else
#         {
#             return false;
#         }
#     }
# 
#     public int hashCode()
#     {
#         return trackedEntity.entityId;
#     }
# 
#     public void updatePlayerList(List list)
#     {
#         playerEntitiesUpdated = false;
#         if(!firstUpdateDone || trackedEntity.getDistanceSq(lastTrackedEntityPosX, lastTrackedEntityPosY, lastTrackedEntityPosZ) > 16D)
#         {
#             lastTrackedEntityPosX = trackedEntity.posX;
#             lastTrackedEntityPosY = trackedEntity.posY;
#             lastTrackedEntityPosZ = trackedEntity.posZ;
#             firstUpdateDone = true;
#             playerEntitiesUpdated = true;
#             updatePlayerEntities(list);
#         }
#         field_28165_t++;
#         if(++updateCounter % field_9234_e == 0 || trackedEntity.isAirBorne)
#         {
#             int i = MathHelper.floor_double(trackedEntity.posX * 32D);
#             int j = MathHelper.floor_double(trackedEntity.posY * 32D);
#             int k = MathHelper.floor_double(trackedEntity.posZ * 32D);
#             int l = MathHelper.floor_float((trackedEntity.rotationYaw * 256F) / 360F);
#             int i1 = MathHelper.floor_float((trackedEntity.rotationPitch * 256F) / 360F);
#             int j1 = i - encodedPosX;
#             int k1 = j - encodedPosY;
#             int l1 = k - encodedPosZ;
#             Object obj = null;
#             boolean flag = Math.abs(j1) >= 4 || Math.abs(k1) >= 4 || Math.abs(l1) >= 4;
#             boolean flag1 = Math.abs(l - encodedRotationYaw) >= 4 || Math.abs(i1 - encodedRotationPitch) >= 4;
#             if(j1 < -128 || j1 >= 128 || k1 < -128 || k1 >= 128 || l1 < -128 || l1 >= 128 || field_28165_t > 400)
#             {
#                 field_28165_t = 0;
#                 trackedEntity.posX = (double)i / 32D;
#                 trackedEntity.posY = (double)j / 32D;
#                 trackedEntity.posZ = (double)k / 32D;
#                 obj = new Packet34EntityTeleport(trackedEntity.entityId, i, j, k, (byte)l, (byte)i1);
#             } else
#             if(flag && flag1)
#             {
#                 obj = new Packet33RelEntityMoveLook(trackedEntity.entityId, (byte)j1, (byte)k1, (byte)l1, (byte)l, (byte)i1);
#             } else
#             if(flag)
#             {
#                 obj = new Packet31RelEntityMove(trackedEntity.entityId, (byte)j1, (byte)k1, (byte)l1);
#             } else
#             if(flag1)
#             {
#                 obj = new Packet32EntityLook(trackedEntity.entityId, (byte)l, (byte)i1);
#             }
#             if(shouldSendMotionUpdates)
#             {
#                 double d = trackedEntity.motionX - lastTrackedEntityMotionX;
#                 double d1 = trackedEntity.motionY - lastTrackedEntityMotionY;
#                 double d2 = trackedEntity.motionZ - lastTrackedEntityMotionZ;
#                 double d3 = 0.02D;
#                 double d4 = d * d + d1 * d1 + d2 * d2;
#                 if(d4 > d3 * d3 || d4 > 0.0D && trackedEntity.motionX == 0.0D && trackedEntity.motionY == 0.0D && trackedEntity.motionZ == 0.0D)
#                 {
#                     lastTrackedEntityMotionX = trackedEntity.motionX;
#                     lastTrackedEntityMotionY = trackedEntity.motionY;
#                     lastTrackedEntityMotionZ = trackedEntity.motionZ;
#                     sendPacketToTrackedPlayers(new Packet28EntityVelocity(trackedEntity.entityId, lastTrackedEntityMotionX, lastTrackedEntityMotionY, lastTrackedEntityMotionZ));
#                 }
#             }
#             if(obj != null)
#             {
#                 sendPacketToTrackedPlayers(((Packet) (obj)));
#             }
#             DataWatcher datawatcher = trackedEntity.getDataWatcher();
#             if(datawatcher.hasObjectChanged())
#             {
#                 sendPacketToTrackedPlayersAndTrackedEntity(new Packet40EntityMetadata(trackedEntity.entityId, datawatcher));
#             }
#             if(flag)
#             {
#                 encodedPosX = i;
#                 encodedPosY = j;
#                 encodedPosZ = k;
#             }
#             if(flag1)
#             {
#                 encodedRotationYaw = l;
#                 encodedRotationPitch = i1;
#             }
#         }
#         trackedEntity.isAirBorne = false;
#         if(trackedEntity.beenAttacked)
#         {
#             sendPacketToTrackedPlayersAndTrackedEntity(new Packet28EntityVelocity(trackedEntity));
#             trackedEntity.beenAttacked = false;
#         }
#     }
# 
#     public void sendPacketToTrackedPlayers(Packet packet)
#     {
#         EntityPlayerMP entityplayermp;
#         for(Iterator iterator = trackedPlayers.iterator(); iterator.hasNext(); entityplayermp.playerNetServerHandler.sendPacket(packet))
#         {
#             entityplayermp = (EntityPlayerMP)iterator.next();
#         }
# 
#     }
# 
#     public void sendPacketToTrackedPlayersAndTrackedEntity(Packet packet)
#     {
#         sendPacketToTrackedPlayers(packet);
#         if(trackedEntity instanceof EntityPlayerMP)
#         {
#             ((EntityPlayerMP)trackedEntity).playerNetServerHandler.sendPacket(packet);
#         }
#     }
# 
#     public void sendDestroyEntityPacketToTrackedPlayers()
#     {
#         sendPacketToTrackedPlayers(new Packet29DestroyEntity(trackedEntity.entityId));
#     }
# 
#     public void removeFromTrackedPlayers(EntityPlayerMP entityplayermp)
#     {
#         if(trackedPlayers.contains(entityplayermp))
#         {
#             trackedPlayers.remove(entityplayermp);
#         }
#     }
# 
#     public void updatePlayerEntity(EntityPlayerMP entityplayermp)
#     {
#         if(entityplayermp == trackedEntity)
#         {
#             return;
#         }
#         double d = entityplayermp.posX - (double)(encodedPosX / 32);
#         double d1 = entityplayermp.posZ - (double)(encodedPosZ / 32);
#         if(d >= (double)(-trackingDistanceThreshold) && d <= (double)trackingDistanceThreshold && d1 >= (double)(-trackingDistanceThreshold) && d1 <= (double)trackingDistanceThreshold)
#         {
#             if(!trackedPlayers.contains(entityplayermp))
#             {
#                 trackedPlayers.add(entityplayermp);
#                 entityplayermp.playerNetServerHandler.sendPacket(getSpawnPacket());
#                 if(shouldSendMotionUpdates)
#                 {
#                     entityplayermp.playerNetServerHandler.sendPacket(new Packet28EntityVelocity(trackedEntity.entityId, trackedEntity.motionX, trackedEntity.motionY, trackedEntity.motionZ));
#                 }
#                 ItemStack aitemstack[] = trackedEntity.getInventory();
#                 if(aitemstack != null)
#                 {
#                     for(int i = 0; i < aitemstack.length; i++)
#                     {
#                         entityplayermp.playerNetServerHandler.sendPacket(new Packet5PlayerInventory(trackedEntity.entityId, i, aitemstack[i]));
#                     }
# 
#                 }
#                 if(trackedEntity instanceof EntityPlayer)
#                 {
#                     EntityPlayer entityplayer = (EntityPlayer)trackedEntity;
#                     if(entityplayer.isPlayerSleeping())
#                     {
#                         entityplayermp.playerNetServerHandler.sendPacket(new Packet17Sleep(trackedEntity, 0, MathHelper.floor_double(trackedEntity.posX), MathHelper.floor_double(trackedEntity.posY), MathHelper.floor_double(trackedEntity.posZ)));
#                     }
#                 }
#                 if(trackedEntity instanceof EntityLiving)
#                 {
#                     EntityLiving entityliving = (EntityLiving)trackedEntity;
#                     PotionEffect potioneffect;
#                     for(Iterator iterator = entityliving.func_35183_ak().iterator(); iterator.hasNext(); entityplayermp.playerNetServerHandler.sendPacket(new Packet41EntityEffect(trackedEntity.entityId, potioneffect)))
#                     {
#                         potioneffect = (PotionEffect)iterator.next();
#                     }
# 
#                 }
#             }
#         } else
#         if(trackedPlayers.contains(entityplayermp))
#         {
#             trackedPlayers.remove(entityplayermp);
#             entityplayermp.playerNetServerHandler.sendPacket(new Packet29DestroyEntity(trackedEntity.entityId));
#         }
#     }
# 
#     public void updatePlayerEntities(List list)
#     {
#         for(int i = 0; i < list.size(); i++)
#         {
#             updatePlayerEntity((EntityPlayerMP)list.get(i));
#         }
# 
#     }
# 
#     private Packet getSpawnPacket()
#     {
#         if(trackedEntity.isDead)
#         {
#             System.out.println("Fetching addPacket for removed entity");
#         }
#         if(trackedEntity instanceof EntityItem)
#         {
#             EntityItem entityitem = (EntityItem)trackedEntity;
#             Packet21PickupSpawn packet21pickupspawn = new Packet21PickupSpawn(entityitem);
#             entityitem.posX = (double)packet21pickupspawn.xPosition / 32D;
#             entityitem.posY = (double)packet21pickupspawn.yPosition / 32D;
#             entityitem.posZ = (double)packet21pickupspawn.zPosition / 32D;
#             return packet21pickupspawn;
#         }
#         if(trackedEntity instanceof EntityPlayerMP)
#         {
#             return new Packet20NamedEntitySpawn((EntityPlayer)trackedEntity);
#         }
#         if(trackedEntity instanceof EntityMinecart)
#         {
#             EntityMinecart entityminecart = (EntityMinecart)trackedEntity;
#             if(entityminecart.minecartType == 0)
#             {
#                 return new Packet23VehicleSpawn(trackedEntity, 10);
#             }
#             if(entityminecart.minecartType == 1)
#             {
#                 return new Packet23VehicleSpawn(trackedEntity, 11);
#             }
#             if(entityminecart.minecartType == 2)
#             {
#                 return new Packet23VehicleSpawn(trackedEntity, 12);
#             }
#         }
#         if(trackedEntity instanceof EntityBoat)
#         {
#             return new Packet23VehicleSpawn(trackedEntity, 1);
#         }
#         if(trackedEntity instanceof IAnimals)
#         {
#             return new Packet24MobSpawn((EntityLiving)trackedEntity);
#         }
#         if(trackedEntity instanceof EntityDragon)
#         {
#             return new Packet24MobSpawn((EntityLiving)trackedEntity);
#         }
#         if(trackedEntity instanceof EntityFishHook)
#         {
#             return new Packet23VehicleSpawn(trackedEntity, 90);
#         }
#         if(trackedEntity instanceof EntityArrow)
#         {
#             Entity entity = ((EntityArrow)trackedEntity).shootingEntity;
#             return new Packet23VehicleSpawn(trackedEntity, 60, entity == null ? trackedEntity.entityId : entity.entityId);
#         }
#         if(trackedEntity instanceof EntitySnowball)
#         {
#             return new Packet23VehicleSpawn(trackedEntity, 61);
#         }
#         if(trackedEntity instanceof EntityPotion)
#         {
#             return new Packet23VehicleSpawn(trackedEntity, 73, ((EntityPotion)trackedEntity).func_40054_n_());
#         }
#         if(trackedEntity instanceof EntityEnderPearl)
#         {
#             return new Packet23VehicleSpawn(trackedEntity, 65);
#         }
#         if(trackedEntity instanceof EntityEnderEye)
#         {
#             return new Packet23VehicleSpawn(trackedEntity, 72);
#         }
#         if(trackedEntity instanceof EntitySmallFireball)
#         {
#             EntitySmallFireball entitysmallfireball = (EntitySmallFireball)trackedEntity;
#             Packet23VehicleSpawn packet23vehiclespawn = null;
#             if(entitysmallfireball.shootingEntity != null)
#             {
#                 packet23vehiclespawn = new Packet23VehicleSpawn(trackedEntity, 64, entitysmallfireball.shootingEntity.entityId);
#             } else
#             {
#                 packet23vehiclespawn = new Packet23VehicleSpawn(trackedEntity, 64, 0);
#             }
#             packet23vehiclespawn.field_28044_e = (int)(entitysmallfireball.accelerationX * 8000D);
#             packet23vehiclespawn.field_28043_f = (int)(entitysmallfireball.accelerationY * 8000D);
#             packet23vehiclespawn.field_28042_g = (int)(entitysmallfireball.accelerationZ * 8000D);
#             return packet23vehiclespawn;
#         }
#         if(trackedEntity instanceof EntityFireball)
#         {
#             EntityFireball entityfireball = (EntityFireball)trackedEntity;
#             Packet23VehicleSpawn packet23vehiclespawn1 = null;
#             if(entityfireball.shootingEntity != null)
#             {
#                 packet23vehiclespawn1 = new Packet23VehicleSpawn(trackedEntity, 63, ((EntityFireball)trackedEntity).shootingEntity.entityId);
#             } else
#             {
#                 packet23vehiclespawn1 = new Packet23VehicleSpawn(trackedEntity, 63, 0);
#             }
#             packet23vehiclespawn1.field_28044_e = (int)(entityfireball.accelerationX * 8000D);
#             packet23vehiclespawn1.field_28043_f = (int)(entityfireball.accelerationY * 8000D);
#             packet23vehiclespawn1.field_28042_g = (int)(entityfireball.accelerationZ * 8000D);
#             return packet23vehiclespawn1;
#         }
#         if(trackedEntity instanceof EntityEgg)
#         {
#             return new Packet23VehicleSpawn(trackedEntity, 62);
#         }
#         if(trackedEntity instanceof EntityTNTPrimed)
#         {
#             return new Packet23VehicleSpawn(trackedEntity, 50);
#         }
#         if(trackedEntity instanceof EntityEnderCrystal)
#         {
#             return new Packet23VehicleSpawn(trackedEntity, 51);
#         }
#         if(trackedEntity instanceof EntityFallingSand)
#         {
#             EntityFallingSand entityfallingsand = (EntityFallingSand)trackedEntity;
#             if(entityfallingsand.blockID == Block.sand.blockID)
#             {
#                 return new Packet23VehicleSpawn(trackedEntity, 70);
#             }
#             if(entityfallingsand.blockID == Block.gravel.blockID)
#             {
#                 return new Packet23VehicleSpawn(trackedEntity, 71);
#             }
#             if(entityfallingsand.blockID == Block.field_41002_bK.blockID)
#             {
#                 return new Packet23VehicleSpawn(trackedEntity, 74);
#             }
#         }
#         if(trackedEntity instanceof EntityPainting)
#         {
#             return new Packet25EntityPainting((EntityPainting)trackedEntity);
#         }
#         if(trackedEntity instanceof EntityXPOrb)
#         {
#             return new Packet26EntityExpOrb((EntityXPOrb)trackedEntity);
#         } else
#         {
#             throw new IllegalArgumentException((new StringBuilder()).append("Don't know how to add ").append(trackedEntity.getClass()).append("!").toString());
#         }
#     }
# 
#     public void removeTrackedPlayerSymmetric(EntityPlayerMP entityplayermp)
#     {
#         if(trackedPlayers.contains(entityplayermp))
#         {
#             trackedPlayers.remove(entityplayermp);
#             entityplayermp.playerNetServerHandler.sendPacket(new Packet29DestroyEntity(trackedEntity.entityId));
#         }
#     }
# }
