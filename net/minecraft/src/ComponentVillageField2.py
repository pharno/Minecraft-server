# // Decompiled by Jad v1.5.8g. Copyright 2001 Pavel Kouznetsov.
# // Jad home page: http://www.kpdus.com/jad.html
# // Decompiler options: packimports(3) braces deadcode fieldsfirst 
# 
# package net.minecraft.src;
# 
# import java.util.List;
# import java.util.Random;
# 
# // Referenced classes of package net.minecraft.src:
# //            ComponentVillage, StructureBoundingBox, StructureComponent, Block, 
# //            MathHelper, World
# 
# public class ComponentVillageField2 extends ComponentVillage
# {
# 
#     private int field_35400_a;
# 
#     public ComponentVillageField2(int i, Random random, StructureBoundingBox structureboundingbox, int j)
#     {
#         super(i);
#         field_35400_a = -1;
#         coordBaseMode = j;
#         boundingBox = structureboundingbox;
#     }
# 
#     public void buildComponent(StructureComponent structurecomponent, List list, Random random)
#     {
#     }
# 
#     public static ComponentVillageField2 func_35399_a(List list, Random random, int i, int j, int k, int l, int i1)
#     {
#         StructureBoundingBox structureboundingbox = StructureBoundingBox.func_35663_a(i, j, k, 0, 0, 0, 7, 4, 9, l);
#         if(!func_35366_a(structureboundingbox) || StructureComponent.canFitInside(list, structureboundingbox) != null)
#         {
#             return null;
#         } else
#         {
#             return new ComponentVillageField2(i1, random, structureboundingbox, l);
#         }
#     }
# 
#     public boolean addComponentParts(World world, Random random, StructureBoundingBox structureboundingbox)
#     {
#         if(field_35400_a < 0)
#         {
#             field_35400_a = getFoundationLevel(world, structureboundingbox);
#             if(field_35400_a < 0)
#             {
#                 return true;
#             }
#             boundingBox.offset(0, ((field_35400_a - boundingBox.y2) + 4) - 1, 0);
#         }
#         fillWithBlocks(world, structureboundingbox, 0, 1, 0, 6, 4, 8, 0, 0, false);
#         fillWithBlocks(world, structureboundingbox, 1, 0, 1, 2, 0, 7, Block.tilledField.blockID, Block.tilledField.blockID, false);
#         fillWithBlocks(world, structureboundingbox, 4, 0, 1, 5, 0, 7, Block.tilledField.blockID, Block.tilledField.blockID, false);
#         fillWithBlocks(world, structureboundingbox, 0, 0, 0, 0, 0, 8, Block.wood.blockID, Block.wood.blockID, false);
#         fillWithBlocks(world, structureboundingbox, 6, 0, 0, 6, 0, 8, Block.wood.blockID, Block.wood.blockID, false);
#         fillWithBlocks(world, structureboundingbox, 1, 0, 0, 5, 0, 0, Block.wood.blockID, Block.wood.blockID, false);
#         fillWithBlocks(world, structureboundingbox, 1, 0, 8, 5, 0, 8, Block.wood.blockID, Block.wood.blockID, false);
#         fillWithBlocks(world, structureboundingbox, 3, 0, 1, 3, 0, 7, Block.waterMoving.blockID, Block.waterMoving.blockID, false);
#         for(int i = 1; i <= 7; i++)
#         {
#             func_35309_a(world, Block.crops.blockID, MathHelper.func_35476_a(random, 2, 7), 1, 1, i, structureboundingbox);
#             func_35309_a(world, Block.crops.blockID, MathHelper.func_35476_a(random, 2, 7), 2, 1, i, structureboundingbox);
#             func_35309_a(world, Block.crops.blockID, MathHelper.func_35476_a(random, 2, 7), 4, 1, i, structureboundingbox);
#             func_35309_a(world, Block.crops.blockID, MathHelper.func_35476_a(random, 2, 7), 5, 1, i, structureboundingbox);
#         }
# 
#         for(int j = 0; j < 9; j++)
#         {
#             for(int k = 0; k < 7; k++)
#             {
#                 func_35314_b(world, k, 4, j, structureboundingbox);
#                 func_35303_b(world, Block.dirt.blockID, 0, k, -1, j, structureboundingbox);
#             }
# 
#         }
# 
#         return true;
#     }
# }
