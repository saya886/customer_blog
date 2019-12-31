<template>
  <div class="main">
  <header_menu/>
    <div class="layer_1">
      <programs_header/>
    </div>
    <div class="layer_2">
      <program_item_1/>
    </div>
    <div class="layer_3">
      <program_item_1/>
    </div>

    <program_item_2/>
    <program_item_3/>
      <content_item_7/>
    
  </div>
</template>

<script>
import programs_header from '@/components/programs_header.vue'
import program_item_1 from '@/components/program_item_1.vue'
import program_item_2 from '@/components/program_item_2.vue'
import program_item_3 from '@/components/program_item_3.vue'
import content_item_7 from '@/components/content_item_7.vue'
import header_menu from '@/components/header_menu.vue'
export default {
    components: {
        programs_header,
        program_item_1,
        program_item_2,
        program_item_3,
        content_item_7,
        header_menu
    }
}
</script>

<style lang="less" scoped>
.main{
  position: relative;
}
.layer_3{
    z-index: -100;
}
</style>