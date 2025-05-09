# mini-image-bed

for blog image url.

- fastapi: https://fastapi.tiangolo.com/
- sqlite: https://www.sqlite.org/index.html

todo:

- [x] upload image
- [x] get image
- [x] delete image
- [x] get image list
- [x] get image info
- [x] get image count
- [x] get image size
- [x] 自定义的raise异常抛出处理
- [ ] sqlite对接方式
- [ ] 解释器，包装api，实现优雅的限制频率
- [ ] 解释器，包装api，实现优雅的接口请求日志，或者是不是可以同时通过异步的方式把返回也记录下来，这样是最好的。记录到sqlite中吧，需要考虑的事情是，定期的数据备份和数据清理。
- [ ] 图片自动压缩到5MB以内，自动压缩。
- [ ] 支持不同后缀的图片：jpg、png、gif、webp。

