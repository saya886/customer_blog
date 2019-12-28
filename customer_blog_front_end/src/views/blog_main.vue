<template>
  <div class="main">
      <blogs_header/>
      <blogs_detail/>
      <content_item_7/>
    
  </div>
</template>

<script>
import blogs_header from '@/components/blogs_header.vue'
import blogs_detail from '@/components/blogs_detail.vue'

import content_item_7 from '@/components/content_item_7.vue'
export default {
    components: {
        blogs_header,
        blogs_detail,
        content_item_7
    }
}
</script>

<style lang="less" scoped>
// .main{
//   position: relative;
// }
</style>