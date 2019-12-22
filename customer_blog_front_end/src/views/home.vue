<template>
<div class="main">
    <div class="img"></div>
    <home_header/>
    <content_item_1/>
    <content_item_2/>
    <content_item_3/>
    <content_item_4/>
    <content_item_5/>
    <content_item_6/>
    <content_item_7/>
    <home_footer/>
</div>
</template>

<script>
import home_header from '@/components/home_header.vue'
import content_item_1 from '@/components/content_item_1.vue'
import content_item_2 from '@/components/content_item_2.vue'
import content_item_3 from '@/components/content_item_3.vue'
import content_item_4 from '@/components/content_item_4.vue'
import content_item_5 from '@/components/content_item_5.vue'
import content_item_6 from '@/components/content_item_6.vue'
import content_item_7 from '@/components/content_item_7.vue'
import home_footer from '@/components/home_footer.vue'


export default {
    components: {
        home_header,
        content_item_1,
        content_item_2,
        content_item_3,
        content_item_4,
        content_item_5,
        content_item_6,
        content_item_7,
        home_footer
    }
}
</script>

<style lang="less" scoped>
// .main{
//     height: 3000px;
// }
a{ text-decoration:none} 
// .img{
//     position: absolute;
//     // z-index: -100;
//     // background: rgba(0, 128, 0, 0.39);
//     // background:url("../assets/template_index.png") no-repeat;
//     width: 1500px;
//     height: 15000px;
//     // background-size: cover;
//     background-repeat:no-repeat;

// }
// *:not(input) {
//   -webkit-user-select: none;
// }
</style>