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
# //            ComponentNetherBridgePiece, ComponentNetherBridgeStartPiece, StructureBoundingBox, StructureComponent, 
# //            Block, World
# 
# public class ComponentNetherBridgeCrossing2 extends ComponentNetherBridgePiece
# {
# 
#     public ComponentNetherBridgeCrossing2(int i, Random random, StructureBoundingBox structureboundingbox, int j)
#     {
#         super(i);
#         coordBaseMode = j;
#         boundingBox = structureboundingbox;
#     }
# 
#     public void buildComponent(StructureComponent structurecomponent, List list, Random random)
#     {
#         func_40287_a((ComponentNetherBridgeStartPiece)structurecomponent, list, random, 1, 0, true);
#         func_40285_b((ComponentNetherBridgeStartPiece)structurecomponent, list, random, 0, 1, true);
#         func_40288_c((ComponentNetherBridgeStartPiece)structurecomponent, list, random, 0, 1, true);
#     }
# 
#     public static ComponentNetherBridgeCrossing2 func_40303_a(List list, Random random, int i, int j, int k, int l, int i1)
#     {
#         StructureBoundingBox structureboundingbox = StructureBoundingBox.func_35663_a(i, j, k, -1, 0, 0, 5, 7, 5, l);
#         if(!func_40286_a(structureboundingbox) || StructureComponent.canFitInside(list, structureboundingbox) != null)
#         {
#             return null;
#         } else
#         {
#             return new ComponentNetherBridgeCrossing2(i1, random, structureboundingbox, l);
#         }
#     }
# 
#     public boolean addComponentParts(World world, Random random, StructureBoundingBox structureboundingbox)
#     {
#         fillWithBlocks(world, structureboundingbox, 0, 0, 0, 4, 1, 4, Block.netherBrick.blockID, Block.netherBrick.blockID, false);
#         fillWithBlocks(world, structureboundingbox, 0, 2, 0, 4, 5, 4, 0, 0, false);
#         fillWithBlocks(world, structureboundingbox, 0, 2, 0, 0, 5, 0, Block.netherBrick.blockID, Block.netherBrick.blockID, false);
#         fillWithBlocks(world, structureboundingbox, 4, 2, 0, 4, 5, 0, Block.netherBrick.blockID, Block.netherBrick.blockID, false);
#         fillWithBlocks(world, structureboundingbox, 0, 2, 4, 0, 5, 4, Block.netherBrick.blockID, Block.netherBrick.blockID, false);
#         fillWithBlocks(world, structureboundingbox, 4, 2, 4, 4, 5, 4, Block.netherBrick.blockID, Block.netherBrick.blockID, false);
#         fillWithBlocks(world, structureboundingbox, 0, 6, 0, 4, 6, 4, Block.netherBrick.blockID, Block.netherBrick.blockID, false);
#         for(int i = 0; i <= 4; i++)
#         {
#             for(int j = 0; j <= 4; j++)
#             {
#                 func_35303_b(world, Block.netherBrick.blockID, 0, i, -1, j, structureboundingbox);
#             }
# 
#         }
# 
#         return true;
#     }
# }
