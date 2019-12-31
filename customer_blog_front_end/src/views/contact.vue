<template>
  <div>
  <header_menu/>
      <contact_header/>
      <content_item_6/>
      <content_item_5/>
      <content_item_7/>
    
  </div>
</template>

<script>
import contact_header from '@/components/contact_header.vue'
import content_item_5 from '@/components/content_item_5.vue'
import content_item_6 from '@/components/content_item_6.vue'
import content_item_7 from '@/components/content_item_7.vue'
import header_menu from '@/components/header_menu.vue'
export default {
    components: {
        contact_header,
        content_item_5,
        content_item_6,
        content_item_7,
        header_menu
    }
}
</script>

<style lang="less" scoped>

</style>