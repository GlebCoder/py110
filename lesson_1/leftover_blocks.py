'''
I am given a number of blocks.
I should build the tallest valid structure with the blocks and determine the number
of left over blocks.

Input - number of blocks
Output - number of left over blocks

Explicit rules:
The top layer - one block
The upper block has to be supported by at least 4 blocks

Implicit rules:
The second layer - 4 blocks minimum
The third layer - 9 blocks minimum.
So, we can see the pattern - each layer - number of blocks = number of layer X number of layer

Data structure:
It can be nested list - list of lists. Each nested list is a layer.

Algorithm:
1. available blocks first assigned to blocks passed in the function.
2. We calculate how many blocks we need for the current layer.
3. If this amount less than available blocks - available blocks assigned to
to available blocks minus blocks we need for the layer.
4. And we repeat steps 2 and 3.
5. If amount available equals amount of blocks we heed for the current layer,
we return zero for leftovers
6. If amount of available blocks less than amount of blocks we need,
we return amount of available blocks as amount of leftovers.
'''

def get_leftovers(blocks):
    available_blocks = blocks
    layer = 1
    while True:
        blocks_for_layer = layer * layer
        if available_blocks > blocks_for_layer:
            available_blocks -= blocks_for_layer
            layer += 1
        elif available_blocks == blocks_for_layer:
            return 0
        else:
            return available_blocks

print(get_leftovers(5))