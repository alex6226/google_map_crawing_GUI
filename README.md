# google_map_crawing_GUI介紹
## 前言
Google評論相對於其他部落格，擁有較高的可信度，不少人在探索新的店面前第一個動作是打開google map，參考上面的留言及評價，再來做接下來的決定，不管對於店家或是消費者，我們都無法否認google評論所帶來的影響力。因此在這我想寫一個能簡單爬取google評論的app，讓不懂程式的人也能輕鬆的透過這款app將google評論下載下來，並做進一步的探討。
## App介紹
使用python中的tkinter套件(GUI圖形化使用者介面工具包)將寫好的爬蟲程式打包，讓沒有程式基礎的人能透過簡單的滑鼠點擊來實現網路爬蟲，使用流程如下:<br>
1. 輸入要爬取的店家的關鍵字<br>
2. 選取要爬取的店家<br>
3. 資料匯出<br>
## (一) 輸入要爬取的店家的關鍵字
由於可能存在同名的店家，或是店家擁有許多分店，因此第一次的輸入無法確定使用者想要爬取的店家
<p float="left">
  <img src="https://user-images.githubusercontent.com/44692570/150670279-69eea8fc-2047-47dc-babd-7c27fccbc990.png" width="220" height="400"/> 
  <img src="https://user-images.githubusercontent.com/44692570/150670337-11eb20da-810d-464b-92a4-5b51821f563c.png" width="700" height="400"/>
</p><br>

## (二) 選取要爬取的店家
在經過第一次的輸入後，返回相關店家清單
<p float="left">
  <img src="https://user-images.githubusercontent.com/44692570/150670631-b69883a9-69f5-4c85-8ffc-e1b61a8272c5.png" width="220" height="400"/> 
  <img src="https://user-images.githubusercontent.com/44692570/150670649-93ccebc3-0b18-4d88-9042-76d48deaaaef.png" width="700" height="400"/>
</p><br>

## (三) 資料匯出
從清單中選取要爬取的店家，等待約1分鐘(視店家評論多寡決定)，在畫片顯示資料爬取完成後，可至資料夾查看資料
<p float="left">
  <img src="https://user-images.githubusercontent.com/44692570/150670781-2c33677c-b0fc-4c57-9b5b-df181fb80aae.png" width="220" height="400"/> 
  <img src="https://user-images.githubusercontent.com/44692570/150670835-8aec2952-b09f-41d0-ab13-6ccb8b205c5e.png" width="700" height="400"/>
</p><br>

## 爬取資料欄位介紹
<p float="left">
   <img src="https://user-images.githubusercontent.com/44692570/150671143-4dd8cec4-ca0c-47de-ac21-97d55ce93cdc.png" width="600" height="300"/>
</p><br>

- <b>評論者：</b>評論者的google帳戶名稱<br>
- <b>評論者id：</b>評論者的googleid<br>
- <b>評論者狀態：</b>評論者的評論次數及狀態<br> 
- <b>評論者等級：</b>評論者的等級，詳情請看[這裡](https://support.google.com/local-guides/answer/6225851?hl=zh-Hant)<br>
- <b>留言時間：</b>評論者的留言時間，依據抓取資料的時間來看<br>
- <b>留言日期：</b>評論者的留言日期<br>
- <b>評論：</b>評論內容<br>
- <b>評論分數：</b>評論者給店家的分數<br>
