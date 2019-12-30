// vue.config.js
module.exports = {
    // 修改的配置
    // 将baseUrl: '/api',改为baseUrl: '/',
    baseUrl: '/',
    devServer: {
        host: "198.13.41.56",
        proxy: {
            '/media': {
                target: 'http://198.13.41.56:8000',
                changeOrigin: true,
                ws: true,
            }
        }
    }
}