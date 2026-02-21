resource "yandex_compute_disk" "server-01-data-disk" {
  name = "server-01-data-disk"
  type = "network-hdd"
  zone = "ru-central1-b"
  size = "30"
}

resource "yandex_compute_instance" "server-01" {
  name     = "server-01"
  hostname = "server-01"
  resources {
    cores  = 2
    memory = 2
  }

  boot_disk {
    initialize_params {
      image_id = var.default_image
      size     = var.default_disk_size
      type     = "network-hdd"
      name     = "server-01-boot-disk"
    }
  }

  secondary_disk {
    disk_id = yandex_compute_disk.server-01-data-disk.id
  }

  network_interface {
    subnet_id = var.default_subnet
    nat       = true
  }

  metadata = {
    user-data = "${file("./users.txt")}"
  }
}

output "internal_ip" {
  value = yandex_compute_instance.server-01.network_interface.0.ip_address
}
