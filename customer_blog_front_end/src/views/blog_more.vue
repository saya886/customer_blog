<template>
  <div class="main">
  <header_menu_dark/>
      <blogs_header/>

      <blogs_more/>

      <content_item_7/>
    
  </div>
</template>

<script>
import blogs_header from '@/components/blogs_header.vue'
import blogs_more from '@/components/blogs_more.vue'

import content_item_7 from '@/components/content_item_7.vue'
import header_menu_dark from '@/components/header_menu_dark.vue'
export default {
    components: {
        blogs_header,
        blogs_more,
        content_item_7,
        header_menu_dark
    }
}
</script>

<style lang="less" scoped>
// .main{
//   position: relative;
// }
</style>