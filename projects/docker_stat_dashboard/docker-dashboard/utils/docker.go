package utils

import (
    "context"
    "github.com/docker/docker/api/types"
    "github.com/docker/docker/client"
)

func GetContainers() ([]types.Container, error) {
    cli, err := client.NewClientWithOpts(client.FromEnv, client.WithAPIVersionNegotiation())
    if err != nil {
        return nil, err
    }
    
    containers, err := cli.ContainerList(context.Background(), types.ContainerListOptions{All: true})
    if err != nil {
        return nil, err
    }
    
    return containers, nil
}

func GetContainer(id string) (types.ContainerJSON, error) {
    cli, err := client.NewClientWithOpts(client.FromEnv, client.WithAPIVersionNegotiation())
    if err != nil {
        return types.ContainerJSON{}, err
    }
    
    container, err := cli.ContainerInspect(context.Background(), id)
    if err != nil {
        return types.ContainerJSON{}, err
    }
    
    return container, nil
}