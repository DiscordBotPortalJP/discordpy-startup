@bot.command()
async def harapan(ctx):
    await ctx.send("ごふっぁ！！・・・な、何するんですか・・・！")

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
