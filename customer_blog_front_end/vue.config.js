// vue.config.js
module.exports = {
    // 修改的配置
    // 将baseUrl: '/api',改为baseUrl: '/',
    baseUrl: '/',
    devServer: {
        proxy: {
            '/media': {
                target: 'http://127.0.0.1:8000',
                changeOrigin: true,
                ws: true,
            }
        }
    }
}