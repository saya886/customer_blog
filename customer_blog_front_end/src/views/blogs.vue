<template>
  <div class="main">
      <blogs_header/>

      <blogs_item_1/>
<blogs_item_2/>

      <content_item_7/>
    
  </div>
</template>

<script>
import blogs_header from '@/components/blogs_header.vue'
import blogs_item_1 from '@/components/blogs_item_1.vue'
import blogs_item_2 from '@/components/blogs_item_2.vue'

import content_item_7 from '@/components/content_item_7.vue'
export default {
    components: {
        blogs_header,
        blogs_item_1,
        blogs_item_2,
        content_item_7
    }
}
</script>

<style lang="less" scoped>
// .main{
//   position: relative;
// }
</style>