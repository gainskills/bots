from bots.botsconfig import *
from .records005040 import recorddefs

syntax = {
    'version': '00504',
    'functionalgroup': 'SC',
    }

structure = [
{ID: 'ST', MIN: 1, MAX: 1, LEVEL: [
    {ID: 'BCT', MIN: 1, MAX: 1},
    {ID: 'CTP', MIN: 0, MAX: 100},
    {ID: 'REF', MIN: 0, MAX: 99999},
    {ID: 'YNQ', MIN: 0, MAX: 10},
    {ID: 'PER', MIN: 0, MAX: 99999},
    {ID: 'DTM', MIN: 0, MAX: 10},
    {ID: 'CTB', MIN: 0, MAX: 25},
    {ID: 'CUR', MIN: 0, MAX: 5},
    {ID: 'ITD', MIN: 0, MAX: 2},
    {ID: 'LDT', MIN: 0, MAX: 99999},
    {ID: 'SAC', MIN: 0, MAX: 99999},
    {ID: 'TD1', MIN: 0, MAX: 99999},
    {ID: 'TD5', MIN: 0, MAX: 99999},
    {ID: 'TD3', MIN: 0, MAX: 99999},
    {ID: 'TD4', MIN: 0, MAX: 99999},
    {ID: 'FOB', MIN: 0, MAX: 1},
    {ID: 'PKG', MIN: 0, MAX: 99999},
    {ID: 'TXI', MIN: 0, MAX: 99999},
    {ID: 'AAA', MIN: 0, MAX: 1},
    {ID: 'MTX', MIN: 0, MAX: 99999},
    {ID: 'PWK', MIN: 0, MAX: 25},
    {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'N2', MIN: 0, MAX: 2},
        {ID: 'N3', MIN: 0, MAX: 2},
        {ID: 'N4', MIN: 0, MAX: 99999},
        {ID: 'REF', MIN: 0, MAX: 12},
        {ID: 'PKG', MIN: 0, MAX: 99999},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'MTX', MIN: 0, MAX: 99999},
        {ID: 'SPI', MIN: 0, MAX: 1},
    ]},
    {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'LQ', MIN: 1, MAX: 99999},
    ]},
    {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'DTM', MIN: 0, MAX: 99999},
        {ID: 'MTX', MIN: 0, MAX: 99999},
        {ID: 'PWK', MIN: 0, MAX: 99999},
        {ID: 'EFI', MIN: 0, MAX: 99999},
    ]},
    {ID: 'G93', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'SAC', MIN: 0, MAX: 1},
        {ID: 'N1', MIN: 0, MAX: 1},
        {ID: 'G26', MIN: 0, MAX: 1},
    ]},
    {ID: 'LIN', MIN: 0, MAX: 99999, LEVEL: [
        {ID: 'PO1', MIN: 0, MAX: 1},
        {ID: 'G53', MIN: 0, MAX: 1},
        {ID: 'SI', MIN: 0, MAX: 99999},
        {ID: 'DTM', MIN: 0, MAX: 10},
        {ID: 'REF', MIN: 0, MAX: 99999},
        {ID: 'YNQ', MIN: 0, MAX: 10},
        {ID: 'PER', MIN: 0, MAX: 99999},
        {ID: 'CRD', MIN: 0, MAX: 99999},
        {ID: 'CTB', MIN: 0, MAX: 25},
        {ID: 'PID', MIN: 0, MAX: 200},
        {ID: 'MEA', MIN: 0, MAX: 200},
        {ID: 'PKG', MIN: 0, MAX: 25},
        {ID: 'PO4', MIN: 0, MAX: 1},
        {ID: 'TD1', MIN: 0, MAX: 99999},
        {ID: 'TD5', MIN: 0, MAX: 99999},
        {ID: 'TD3', MIN: 0, MAX: 99999},
        {ID: 'TD4', MIN: 0, MAX: 99999},
        {ID: 'ITD', MIN: 0, MAX: 2},
        {ID: 'LDT', MIN: 0, MAX: 1},
        {ID: 'SAC', MIN: 0, MAX: 99999},
        {ID: 'FOB', MIN: 0, MAX: 1},
        {ID: 'AAA', MIN: 0, MAX: 1},
        {ID: 'TC2', MIN: 0, MAX: 2},
        {ID: 'TXI', MIN: 0, MAX: 99999},
        {ID: 'MTX', MIN: 0, MAX: 99999},
        {ID: 'G55', MIN: 0, MAX: 1},
        {ID: 'G54', MIN: 0, MAX: 1},
        {ID: 'CTP', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'G36', MIN: 0, MAX: 1},
            {ID: 'LDT', MIN: 0, MAX: 1},
            {ID: 'CUR', MIN: 0, MAX: 5},
            {ID: 'PO4', MIN: 0, MAX: 1},
            {ID: 'CTB', MIN: 0, MAX: 5},
            {ID: 'REF', MIN: 0, MAX: 99999},
            {ID: 'G43', MIN: 0, MAX: 9999},
            {ID: 'SAC', MIN: 0, MAX: 99999},
            {ID: 'G26', MIN: 0, MAX: 99},
            {ID: 'TXI', MIN: 0, MAX: 99999},
            {ID: 'ITD', MIN: 0, MAX: 1},
            {ID: 'G40', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'SAC', MIN: 0, MAX: 1},
                {ID: 'G93', MIN: 0, MAX: 99999},
            ]},
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'LM', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'LQ', MIN: 1, MAX: 99999},
                ]},
                {ID: 'LE', MIN: 1, MAX: 1},
            ]},
            {ID: 'LS', MIN: 0, MAX: 1, LEVEL: [
                {ID: 'N1', MIN: 1, MAX: 99999, LEVEL: [
                    {ID: 'N2', MIN: 0, MAX: 2},
                    {ID: 'N3', MIN: 0, MAX: 2},
                    {ID: 'N4', MIN: 0, MAX: 2},
                ]},
                {ID: 'LE', MIN: 1, MAX: 1},
            ]},
        ]},
        {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'N2', MIN: 0, MAX: 2},
            {ID: 'N3', MIN: 0, MAX: 2},
            {ID: 'N4', MIN: 0, MAX: 1},
            {ID: 'REF', MIN: 0, MAX: 12},
            {ID: 'PER', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 10},
            {ID: 'MTX', MIN: 0, MAX: 99999},
            {ID: 'PKG', MIN: 0, MAX: 99999},
            {ID: 'PAL', MIN: 0, MAX: 99999},
            {ID: 'SPI', MIN: 0, MAX: 1},
        ]},
        {ID: 'G39', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'CTP', MIN: 0, MAX: 1},
        ]},
        {ID: 'PKL', MIN: 0, MAX: 20, LEVEL: [
            {ID: 'CTP', MIN: 0, MAX: 1},
            {ID: 'PKG', MIN: 0, MAX: 2},
            {ID: 'G53', MIN: 0, MAX: 1},
            {ID: 'DTM', MIN: 0, MAX: 99999},
        ]},
        {ID: 'LFG', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'CRC', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'QTY', MIN: 0, MAX: 1},
            ]},
        ]},
        {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'LQ', MIN: 1, MAX: 99999, LEVEL: [
                {ID: 'REF', MIN: 0, MAX: 99999},
                {ID: 'EFI', MIN: 0, MAX: 1},
                {ID: 'DTM', MIN: 0, MAX: 99999},
                {ID: 'PID', MIN: 0, MAX: 99999, LEVEL: [
                    {ID: 'MEA', MIN: 0, MAX: 99999},
                    {ID: 'MTX', MIN: 0, MAX: 1},
                ]},
            ]},
        ]},
        {ID: 'SLN', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'SI', MIN: 0, MAX: 99999},
            {ID: 'PID', MIN: 0, MAX: 99999},
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'CTP', MIN: 0, MAX: 99999},
            {ID: 'PAM', MIN: 0, MAX: 99999},
            {ID: 'PO4', MIN: 0, MAX: 99999},
            {ID: 'PKG', MIN: 0, MAX: 99999},
            {ID: 'QTY', MIN: 0, MAX: 99999},
            {ID: 'MEA', MIN: 0, MAX: 99999},
            {ID: 'SAC', MIN: 0, MAX: 99999},
            {ID: 'MTX', MIN: 0, MAX: 99999},
            {ID: 'LM', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'LQ', MIN: 1, MAX: 99999},
            ]},
            {ID: 'N1', MIN: 0, MAX: 99999, LEVEL: [
                {ID: 'N2', MIN: 0, MAX: 2},
                {ID: 'N3', MIN: 0, MAX: 2},
                {ID: 'N4', MIN: 0, MAX: 99999},
                {ID: 'REF', MIN: 0, MAX: 12},
                {ID: 'PER', MIN: 0, MAX: 99999},
                {ID: 'DTM', MIN: 0, MAX: 10},
            ]},
        ]},
        {ID: 'N9', MIN: 0, MAX: 99999, LEVEL: [
            {ID: 'DTM', MIN: 0, MAX: 99999},
            {ID: 'MTX', MIN: 0, MAX: 99999},
            {ID: 'PWK', MIN: 0, MAX: 99999},
            {ID: 'EFI', MIN: 0, MAX: 99999},
        ]},
    ]},
    {ID: 'CTT', MIN: 0, MAX: 1},
    {ID: 'SE', MIN: 1, MAX: 1},
]}
]
