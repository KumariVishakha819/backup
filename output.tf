#comment
//comment
output "firstblock"{
    value = var.nameslist[1]
}
output "secondblock"{
    value = var.username
}

output "url"{
    value = github_repository.terraform_first_repo.html_url
}