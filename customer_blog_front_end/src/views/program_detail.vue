<template>
  <div>
  <header_menu/>
      <program_deatil_item_1/>
      <program_deatil_item_2/>
      <content_item_7/>
    
  </div>
</template>

<script>
import header_menu from '@/components/header_menu.vue'
import program_detail_header from '@/components/program_detail_header.vue'
import program_deatil_item_1 from '@/components/program_deatil_item_1.vue'
import program_deatil_item_2 from '@/components/program_deatil_item_2.vue'
import content_item_7 from '@/components/content_item_7.vue'

export default {
    components: {
        header_menu,
        program_detail_header,
        program_deatil_item_1,
program_deatil_item_2,
content_item_7

    }
}
</script>

<style lang="less" scoped>

</style>