<template>
    <div class="btn-box">
        <h3>文件上传：</h3>
        <input class="file-input" type="file" @change="getFile($event)" />
        <el-button type="primary" @click="upload">上传文件(POST)</el-button>
        <h3>文件下载：</h3>
        <el-button type="primary" @click="downloadLink">下载带链接文件(window.open)</el-button>
        <el-button type="primary" @click="downloadBlobByGet">二进制流下载(GET)</el-button>
        <el-button type="primary" @click="downloadBlobByPost">二进制流下载(POST)</el-button>
    </div>
</template>

<script>
    import axios from "axios"
    export default {
        name: "attendPoint",
        data() {
            return {
                file: null,
                fileName: ""
            }
        },
        methods: {
            // 选取文件
            getFile(event) {
                this.file = event.target.files[0];
            },

            // 上传文件(POST)
            upload() {
                let url = "http://localhost:8000/upload";
                let formData = new FormData();
                formData.append("name", "zhangsan");
                formData.append("age", "18");
                formData.append("token", "test_token");
                formData.append("file", this.file);
                let config = {
                    headers: {
                        "Content-Type": "multipart/form-data"
                    }
                }
                axios.post(url, formData, config).then((res) => {
                    this.fileName = res.data.filename;
                    console.log(res)
                    alert("上传成功!");
                }).catch(() => {
                    alert("请先上传文件!");
                })
            },

            // 下载带链接文件 (window.open)
            downloadLink() {
                if (this.fileName) {
                    window.open("http://localhost:8000/download?filename=" + this.fileName);
                }
            },

            // 二进制流下载(GET)
            // async downloadBlobByGet() {
            //     let urlGet = "http://localhost:8000/download?filename=" + this.fileName;
            //     let fileData = await axios.get(urlGet, { responseType: "blob" });
            //     let URL = window.URL || window.webkitURL;
            //     let downloadUrl = URL.createObjectURL(fileData.data);
            //     let a = document.createElement("a");
            //     a.href = downloadUrl;
            //     a.download = this.fileName;//下载后文件名
            //     a.click();
            //     a = null;
            //     downloadUrl && URL.revokeObjectURL(downloadUrl);
            // },

            // 二进制流下载(POST)
            // async downloadBlobByPost() {
            //     let urlPost = "http://localhost:3000/download/post/test";
            //     let fileData = await axios({
            //         method: "post",
            //         url: urlPost, // 请求地址
            //         data: { fileName: this.fileName }, // 参数
            //         responseType: "blob" // 表明返回服务器返回的数据类型
            //     })
            //     let URL = window.URL || window.webkitURL;
            //     let downloadUrl = URL.createObjectURL(fileData.data);
            //     let a = document.createElement("a");
            //     a.download = this.fileName;
            //     a.href = downloadUrl;
            //     a.click();
            //     a = null;
            //     downloadUrl && URL.revokeObjectURL(downloadUrl);
            // },
        },
    }
</script>

<style scoped>
    .btn-box {
        padding: 20px;
    }
    .el-button,
    input {
        max-width: fit-content;
        display: block;
        margin: 20px;
    }
</style>