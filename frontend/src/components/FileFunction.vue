<template>
    <div class="module-box">
        <h3 class="box-title">模型输入</h3>
        <div class="box-content">
            <div id="file-select">
                <input id="file-input" type="file" @change="getFile($event)" />
                <label type="button" for="file-input" class="upload-btn">
                    选择文件
                </label>
                <span class="file-name">{{fileName}}</span>
            </div>
            <el-button class="file-btn" type="primary" @click="upload">上传文件(POST)</el-button>
        </div>
    </div>
    <div class="module-box">
        <h3 class="box-title">模型输出</h3>
        <div class="box-content">
            <el-button class="file-btn" type="primary" @click="downloadLink">下载带链接文件(window.open)</el-button>
        </div>
    </div>
</template>

<script>
    import axios from "axios"
    export default {
        name: "attendPoint",
        data() {
            return {
                file: null,
                fileName: "未选择文件"
            }
        },
        methods: {
            // 选取文件
            getFile(event) {
                this.file = event.target.files[0];
                alert(this.file.name);
            },

            // 上传文件 (POST)
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
        },
    }
</script>

<style scoped>
    .module-box {
        /* padding: 20px; */
        background-color: aqua;
    }

    .box-title {
        background-color: brown;
        font-family: Arial, Helvetica, sans-serif;
        font-weight: bold;
        color: white;
        padding: 10px 30px;
    }

    .box-content {
        padding: 30px;
        background-color: grey;
    }

    #file-select {
        height: 100px;
    }

    .upload-btn {
        background-color: green;
        /* padding: 0 10px; */
        text-align: center;
        font-family: Arial, Helvetica, sans-serif;
        font-size: 1.1em;
        /* font-weight: bold; */
        color: white;
        display: block;
        width: 150px;
        height: 50px;
        line-height: 48px; /* 需为 height 减去上下边框 */
        float: left;
        border-style: solid;
        border-color: green;
        border-width: 1px 1px 1px 1px;
        border-radius: 10px 0 0 10px;
    }

    .file-name {
        display: block;
        width: 200px;
        font-size: 1.1em;
        padding: 0 15px;
        height: 50px;
        line-height: 48px; /* 需为 height 减去上下边框 */
        float: left;
        border-style: solid;
        border-width: 1px 1px 1px 0;
        border-color: green;
        border-radius: 0 10px 10px 0;
    }

    .file-btn {
        max-width: fit-content;
        display: block;
        /* margin: 20px; */
        background-color: palevioletred;
        padding: 15px 30px;
        font-family: Arial, Helvetica, sans-serif;
        font-size: 1.1em;
        /* font-weight: bold; */
        color: white;
    }

    #file-input {
        /* max-width: fit-content;
        display: block;
        margin: 20px;
        background-color: aliceblue;
        padding: 10px; */
        display: none;
    }
</style>