import random
#asyncだとだめっぽい
#async def get_harapan():
#    await "ごふっぁ！！・・・な、何するんですか・・・！"
    
def get_harapan():
    #確率の重みとセリフリスト
    msg_list = [
        [100, "いっっ・・・た！！げほっ、ごほっ！"],
        [100, "ごふっぁ！！・・・な、何するんですか・・・！"]
    ]
    
    #総重み
    total_weight = 0
    for i in msg_list:
        total_weight += i[0]
    
    #順番に確率に当てはまるかやっていく
    target = msg_list[0]
    for i in msg_list:
        if  random.randint(0, total_weight) <= i[0]):
            target = i
            break
        total_weight -= i[0]
     
    #セリフ部分を返す
    return target[1]
"""

client.on('message', message =>{
  if (message.author.id == client.user.id || message.author.bot){
    return;
  }
  if (message.content.match(/^！おみくじ/) ||
      (message.isMemberMentioned(client.user) && message.content.match(/おみくじ/))){
    let arr = ["大吉", "吉", "凶", "ぽてと", "にゃ～ん", "しゅうまい君"];
    let weight = [5, 30, 10, 15, 20, 20];
    lotteryByWeight(message.channel.id, arr, weight);
  }else if (message.isMemberMentioned(client.user)){
    sendReply(message, "呼びましたか？");
  }
});

function lotteryByWeight(channelId, arr, weight){
  let totalWeight = 0;
  for (var i = 0; i < weight.length; i++){
    totalWeight += weight[i];
  }
  let random = Math.floor(Math.random() * totalWeight);
  for (var i = 0; i < weight.length; i++){
    if (random < weight[i]){
      sendMsg(channelId, arr[i]);
      return;
    }else{
      random -= weight[i];
    }
  }
  console.log("lottery error");
}
"""
