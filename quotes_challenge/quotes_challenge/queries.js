db.getCollection("joao_lima").find({}).count();

db.getCollection("joao_lima").distinct("tags")

db.getCollection("joao_lima").distinct("tags").length

db.getCollection("joao_lima").aggregate({$group : { _id : '$author', qtd: {$sum : 1}}});