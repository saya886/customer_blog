<template>
  <div class="main">
    <div class="layer_1">
      <about_header/>
    </div>
    <div class="layer_2">
      <about_item_1/>
    </div>
      
      
      <about_item_2/>
      <about_item_3/>
       <about_item_4/>
       <about_item_5/>
      <content_item_7/>
    
  </div>
</template>

<script>
import about_header from '@/components/about_header.vue'
import about_item_1 from '@/components/about_item_1.vue'
import about_item_2 from '@/components/about_item_2.vue'
import about_item_3 from '@/components/about_item_3.vue'
import about_item_4 from '@/components/about_item_4.vue'
import about_item_5 from '@/components/about_item_5.vue'
import content_item_7 from '@/components/content_item_7.vue'
export default {
    components: {
        about_header,
        about_item_1,
        about_item_2,
        about_item_3,
        about_item_4,
        about_item_5,
        content_item_7
    }
}
</script>

<style lang="less" scoped>
.main{
  position: relative;
}
</style>